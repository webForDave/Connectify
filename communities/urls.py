from django.urls import path
from . import views

urlpatterns = [
    path("communities/create/", views.create_community_view, name="create_community"),
    path("", views.home, name="home"),
    path("communities/<slug:slug>/", views.community_detail_view, name="community_detail")
]
