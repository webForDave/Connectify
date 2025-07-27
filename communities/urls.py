from django.urls import path
from . import views

urlpatterns = [
    path("communities/create/", views.create_community_view, name="create_community"),
    path("communities/", views.list_communities_view, name="communities"),
]
