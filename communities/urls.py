from . import views
from django.urls import path

urlpatterns = [
    path('', views.community_view_create, name='community_view_create'),
    path('<str:name>/', views.community_detail, name='community_view_create'),
]