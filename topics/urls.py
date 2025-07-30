from . import views
from django.urls import path

urlpatterns = [
    path("topics/<slug:slug>/create/", views.create_new_topic_view, name="create_topic"),
    path("topics/<slug:slug>/", views.topic_detail_view, name="topic_detail"),
    path("topics/<slug:slug>/update/", views.update_topic, name="update_topic"),
    path("topics/<slug:slug>/delete/", views.delete_topic_view, name="delete_topic"),
]
