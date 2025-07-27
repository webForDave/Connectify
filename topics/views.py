from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic
from .forms import CreateTopicForm
from django.contrib.auth.decorators import login_required

def home(request):
    topics = Topic.objects.all()
    return render(request, "topics/home.html", {"topics": topics})

@login_required
def create_new_topic_view(request):
    if request.method == "POST":
        form = CreateTopicForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.save()
            return redirect("home")
    else:
        form = CreateTopicForm()
    return render(request, "topics/create_topic.html", {"form": form})

def topic_detail_view(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, "topics/topic_detail.html", {"topic": topic})