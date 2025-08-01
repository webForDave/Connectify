from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Community
from .forms import CreateCommunityForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def create_community_view(request):
    if request.method == "POST":
        form = CreateCommunityForm(request.POST)
        if form.is_valid():
            community_instance = form.save(commit=False)
            community_instance.author = request.user
            community_instance.save()
            return redirect("home")
    else:
        form = CreateCommunityForm()
    context = {"form": form}
    return render(request, "communities/create_community.html", context)

def home(request):
    communities = Community.objects.all().order_by("-id")
    context = {"communities": communities}
    return render(request, "communities/home.html", context)

def community_detail_view(request, slug):
    community = get_object_or_404(Community, slug=slug)
    topics = community.topic_set.all().order_by("-id") # REVERSE RELATIONSHIP (Parent asking for it's children)
    context = {
        "community": community,
        "topics": topics
    }
    return render(request, "communities/community_detail.html", context)


@login_required
def delete_community_view(request, slug):
    community = get_object_or_404(Community, slug=slug)
    user = request.user
    if request.method == "POST":
        community.delete()
        return redirect("home")
    return render(request, "communities/delete_community.html", {"user": user, "community": community})

@login_required
def update_community_view(request, slug):
    community = get_object_or_404(Community, slug=slug)
    if request.method == "POST":
        form = CreateCommunityForm(request.POST, instance=community)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateCommunityForm(instance=community)
    return render(request, "communities/update_community.html", {"form": form})