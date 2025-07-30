from django.db import models
from django.conf import settings
from autoslug import AutoSlugField

class Community(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True, default="", max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name