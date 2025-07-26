from django.shortcuts import render, redirect
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