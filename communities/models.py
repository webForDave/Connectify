from django.db import models
from django_extensions.db.models import AutoSlugField
from django.contrib.auth import get_user_model

User = get_user_model()

class Community(models.Model):
    community_name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    slug = AutoSlugField(populate_from='community_name', unique=True, overwrite=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='communities_created')
    members = models.ManyToManyField(User, related_name='communities_joined')
    members_count = models.IntegerField(default=0)

    def __str__(self):
        return self.community_name