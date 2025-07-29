from django.forms import ModelForm
from .models import Comment
from django import forms

class CreateCommentForm(ModelForm):
    class Meta:
        fields = ["content"]
        model = Comment 
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500",
                "rows": 4,
                "placeholder": "Write your comment..."
            }),
        }