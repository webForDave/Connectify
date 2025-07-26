from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("profile/<str:username>/", views.user_profile_view, name="user_profile"),
]
