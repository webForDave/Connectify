from django.db import models
from django.conf import settings
from communities.models import Community
from autoslug import AutoSlugField

class Topic(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True, default="")
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title