from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            return redirect("login") 
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/sign_up.html", {"form": form})

def user_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, "registration/user_profile.html", {"user": user})