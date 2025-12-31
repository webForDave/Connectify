# core Django.
from django.contrib import admin

# communities app.
from .models import Community

admin.site.register(Community)