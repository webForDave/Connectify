from django.urls import path
from . import views
from .forms import StyledLoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("profile/<str:username>/", views.user_profile_view, name="user_profile"),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=StyledLoginForm
    ), name='login'),
    path("profile/<str:username>/update/", views.update_profile, name="update_profile"),
]
