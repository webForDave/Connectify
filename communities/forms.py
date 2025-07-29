from .models import Community
from django.forms import ModelForm
from django import forms

class CreateCommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ("name", "description",)
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-indigo-500",
                "placeholder": "Community name"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-indigo-500",
                "rows": 4,
                "placeholder": "Describe your community..."
            }),
        }