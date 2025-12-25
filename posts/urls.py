from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_view_create, name='post_view_create'),
    path('<str:post_title>/', views.post_details, name='post_details'),
]