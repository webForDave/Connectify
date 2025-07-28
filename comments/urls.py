from django.urls import path
from . import views

urlpatterns = [
    path("topics/<slug:slug>/comment/new/", views.create_comment_view, name="create_comment"),
]
