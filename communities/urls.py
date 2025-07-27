from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("communities/create/", views.create_community_view, name="create_community"),
    path("communities/<slug:slug>/", views.community_view, name="community"),
]
