from django.forms import ModelForm
from .models import Comment

class CreateCommentForm(ModelForm):
    class Meta:
        fields = ["content"]
        model = Comment 