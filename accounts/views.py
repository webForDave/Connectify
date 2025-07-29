from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login") 
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/sign_up.html", {"form": form})

def user_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    topics_count = user.topic_set.all().count()
    comments_count = user.comment_set.all().count()
    return render(request, "registration/user_profile.html", {"user": user, "topics_count": topics_count, "comments_count": comments_count})