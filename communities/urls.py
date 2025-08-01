from django.urls import path
from . import views

urlpatterns = [
    path("communities/create/", views.create_community_view, name="create_community"),
    path("", views.home, name="home"),
    path("communities/<slug:slug>/", views.community_detail_view, name="community_detail"),
    path("communities/<slug:slug>/delete/", views.delete_community_view, name="delete_community"),
    path("communities/<slug:slug>/update/", views.update_community_view, name="update_community"),
]
