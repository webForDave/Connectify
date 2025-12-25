from django.db import models
from django.contrib.auth import get_user_model
from communities.models import Community
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts_created')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='community_posts')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title