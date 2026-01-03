from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'vote_count', 'date_created']

class CreatePostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'title', 'content']

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'created_by', 'vote_count', 'date_created', 'post_comments']

class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

class PostCommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'slug', 'parent', 'comment_author', 'vote_count', 'date_created', 'replies']

class UpdateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

class CommentRepliesSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'comment_author', 'post', 'parent', 'date_created']