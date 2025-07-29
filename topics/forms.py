from .models import Topic
from django.forms import ModelForm
from django import forms

class CreateTopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ("title", "content",)
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-indigo-500",
                "placeholder": "Topic title"
            }),
            "content": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-indigo-500",
                "rows": 6,
                "placeholder": "Start the conversation..."
            }),
        }   