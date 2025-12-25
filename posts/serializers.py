from rest_framework.serializers import ModelSerializer
from .models import Post

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'date_created']

class CreatePostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'title', 'content']

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'date_created']