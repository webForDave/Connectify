from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_view_create, name='post_view_create'),
    path('<slug:post_slug>/', views.post_details, name='post_details'),
    path('<slug:post_slug>/comments/', views.comment_view_create, name='post_comments'),
    path('<slug:post_slug>/comments/<int:comment_id>/', views.comment_details, name='comment_details'),
    path('<slug:post_slug>/comments/<int:comment_id>/replies/', views.replies_view_create, name='comment_replies'),
]