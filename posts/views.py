from rest_framework import status
from rest_framework.response import Response
from .models import Post
from communities.models import Community
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostsSerializer, CreatePostSerializer, PostSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_view_create(request, community_name):

    try:
        community = Community.objects.get(community_name__iexact=community_name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = CreatePostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user, community=community)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_details(request, community_name, post_title):
    try:
        community = Community.objects.get(community_name__iexact=community_name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    post = Post.objects.filter(title__iexact=post_title).first()

    if post == None:
        return Response({'posts': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        if request.user != post.created_by:
            return Response({'posts': 'You do not have permission to perform this action'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CreatePostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method == 'DELETE':
        if request.user != post.created_by:
            return Response({'posts': 'You do not have permission to perform this action'}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)