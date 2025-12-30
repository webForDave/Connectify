from rest_framework.serializers import ModelSerializer
from .models import Community

class CommunityCreateSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description']

class CommunitiesViewSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'slug', 'description', 'date_created']

class CommunityViewSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'slug', 'description', 'date_created', 'members_count']

class UpdateCommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description']