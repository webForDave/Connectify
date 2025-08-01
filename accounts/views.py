from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    redirect_to_after_login = request.GET.get('next', '')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login_url = reverse('login')
            if redirect_to_after_login:
                login_url += f"?next={redirect_to_after_login}"
            return redirect(login_url) 
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/sign_up.html", {"form": form, "next_url": redirect_to_after_login})

def user_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    topics_count = user.topic_set.all().count()
    comments_count = user.comment_set.all().count()
    user_topics = user.topic_set.all()
    user_comments = user.comment_set.all()

    context = {
        "user": user,
        "topics_count": topics_count,
        "comments_count": comments_count,
        "user_topics": user_topics,
        "user_comments": user_comments,
    }
    return render(request, "registration/user_profile.html", context)

@login_required
def update_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_profile", username=user.username)
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, "registration/update_profile.html", {"form": form})