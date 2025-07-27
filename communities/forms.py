from .models import Community
from django.forms import ModelForm

class CreateCommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ("name", "description",)