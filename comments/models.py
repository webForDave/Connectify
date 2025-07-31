from django.db import models
from django.conf import settings
from topics.models import Topic
from autoslug import AutoSlugField

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    slug = AutoSlugField(populate_from="content", unique=True, always_update=True, default="")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content