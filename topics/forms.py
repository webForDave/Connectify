from .models import Topic
from django.forms import ModelForm

class CreateTopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ("title", "content",)