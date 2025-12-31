from rest_framework import status
from rest_framework.response import Response
from .models import Post, Comment
from communities.models import Community
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostsSerializer, CreatePostSerializer, PostSerializer, CreateCommentSerializer, PostCommentsSerializer

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
        posts = community.community_posts.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_details(request, community_name, post_slug):
    try:
        community = Community.objects.get(community_name__iexact=community_name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    post = Post.objects.get(
        slug=post_slug,
        community=community)

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
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        if request.user != post.created_by:
            return Response({'posts': 'You do not have permission to perform this action'}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_view_create(request, community_name, post_slug):
    try:
        community = Community.objects.get(community_name__iexact=community_name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return Response({'posts': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostCommentsSerializer(post.post_comments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CreateCommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post_id=post.id, comment_author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_details(request, community_name, post_title, comment_slug):

    try:
        community = Community.objects.get(community_name__iexact=community_name)
    except Community.DoesNotExist:
        return Response({'communities': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        post = Post.objects.get(title__iexact=post_title)
    except Post.DoesNotExist:
        return Response({'posts': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        comment = Comment.objects.get(comment_slug=comment_slug)
    except Comment.DoesNotExist:
        return Response({'comments': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostCommentsSerializer(comment)
        return Response(serializer.data)

    if request.method == 'PUT':
        if request.user != comment.comment_author:
            return Response({'comments': 'You do not have permission to perform this action'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CreateCommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)