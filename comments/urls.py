from django.urls import path
from . import views

urlpatterns = [
    path("topics/<slug:slug>/comment/new/", views.create_comment_view, name="create_comment"),
    path("topics/comment/<slug:slug>/update/", views.update_comment_view, name="update_comment"),
    path("topics/comment/<slug:slug>/delete/", views.delete_comment_view, name="delete_comment"),
]
