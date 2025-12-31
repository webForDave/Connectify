# third party.
from rest_framework.serializers import ModelSerializer

# communities app.
from .models import Community

class CreateCommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description']

class CommunitiesSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'slug', 'description', 'date_created']

class CommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'slug', 'description', 'date_created', 'members_count', 'community_posts']

class UpdateCommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description']