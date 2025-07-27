from django.urls import path
from . import views

urlpatterns = [
    path("communities/create/", views.create_community_view, name="create_community"),
    path("", views.list_communities_view, name="communities"),
    path("communities/<slug:slug>/", views.community_detail_view, name="community_detail")
]
