from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("topics/create/", views.create_new_topic_view, name="create_topic"),
    path("topics/<slug:slug>/", views.topic_detail_view, name="topic_detail")
]
