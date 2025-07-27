from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Community
from .forms import CreateCommunityForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    communities = Community.objects.all()
    return render(request, "communities/home.html", {"communities": communities})

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
        form =CreateCommunityForm()
    return render(request, "communities/create_community.html", {"form": form})

def community_view(request, slug):
    community = get_object_or_404(Community, slug=slug)
    return render(request, "communities/community_view.html", {"community": community})