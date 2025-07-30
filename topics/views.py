from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic
from .forms import CreateTopicForm
from django.contrib.auth.decorators import login_required
from communities.models import Community
from comments.models import Comment

@login_required
def create_new_topic_view(request, slug):
    community = get_object_or_404(Community, slug=slug)
    if request.method == "POST":
        form = CreateTopicForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form.instance.community = community
            form_instance.save()
            return redirect("community_detail", slug=community.slug)
    else:
        form = CreateTopicForm()
    context = {
        "form": form,
        "community": community
    }
    return render(request, "topics/create_topic.html", context)

@login_required
def update_topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    if request.method == "POST":
        form = CreateTopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect("topic_detail", slug=slug)
    else:
        form = CreateTopicForm(instance=topic)
    return render(request, "topics/update_topic.html", {"form": form})

@login_required
def delete_topic_view(request, slug):
    topic = get_object_or_404(Topic, slug=slug)

    if request.method == "POST":
        topic.delete()
        return redirect("home")
    return render(request, "topics/delete_topic.html", {"topic": topic})

def topic_detail_view(request, slug):
    user = request.user
    topic = get_object_or_404(Topic, slug=slug)
    comments = topic.comment_set.all().order_by("-id")
    context = {
        "topic": topic,
        "comments": comments,
        "user": user
    }
    return render(request, "topics/topic_detail.html", context)