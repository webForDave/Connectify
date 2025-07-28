from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic
from .forms import CreateTopicForm
from django.contrib.auth.decorators import login_required
from communities.models import Community

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

def topic_detail_view(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    comments = topic.comment_set.all().order_by("-id")
    context = {
        "topic": topic,
        "comments": comments
    }
    return render(request, "topics/topic_detail.html", context)