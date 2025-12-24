from rest_framework import status
from rest_framework.response import Response
from .models import Community
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from .serializers import CommunityCreateSerializer, CommunitiesViewSerializer, CommunityViewSerializer, UpdateCommunitySerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def community_view_create(request):

    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitiesViewSerializer(communities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CommunityCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            # adding the creator of a community as its first member
            community = Community.objects.filter(id=serializer.data['id']).first()
            community.members.add(request.user)
            community.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def community_detail(request, name):
    try:
        community = Community.objects.get(community_name__iexact=name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        community.members_count = len(community.members.all())
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