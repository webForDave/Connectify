from rest_framework.serializers import ModelSerializer
from .models import Community
from rest_framework import serializers

class CommunityCreateSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description']

class CommunitiesViewSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description', 'date_created']

class CommunityViewSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description', 'date_created', 'members_count']

class UpdateCommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['community_name', 'description']