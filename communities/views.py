from rest_framework import status
from rest_framework.response import Response
from .models import Community
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from .serializers import CommunityCreateSerializer, CommunitiesViewSerializer, CommunityViewSerializer, UpdateCommunitySerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def community_view_create(request):

    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitiesViewSerializer(communities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CommunityCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            community = Community.objects.get(community_name=serializer.validated_data['community_name'])
            community.members.add(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def community_detail(request, name):
    try:
        community = Community.objects.get(community_name__iexact=name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method in ['PUT', 'DELETE']:
        if community.created_by != request.user:
            return Response({'detail': 'You do not have permission to perform this action.'},
                            status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        community.members_count = community.members.all().count()
        community.save()
        serializer = CommunityViewSerializer(community)
        return Response(serializer.data)
    
    if request.method  == 'PUT':
        serializer = UpdateCommunitySerializer(community, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_community(request, name):
    try:
        community = Community.objects.get(community_name__iexact=name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user in community.members.all():
        return Response({'community': 'user already in community'})
    else:
        community.members.add(request.user)
        community.members_count = community.members.all().count()
        community.save()
        return Response({'community': 'success'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def leave_community(request, name):
    try:
        community = Community.objects.get(community_name__iexact=name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user not in community.members.all():
        return Response({'community': 'You are not a member of this community'})
    else:
        community.members.remove(request.user)
        community.members_count = community.members.all().count()
        community.save()
        if community.members_count < 1:
            community.delete()
    return Response({'community': 'success'})
    