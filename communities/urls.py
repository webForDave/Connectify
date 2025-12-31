from . import views
from django.urls import path

urlpatterns = [
    path('', views.community_view_create, name='community_list'),
    path('<slug:community_slug>/join/', views.join_community, name='join_community'),
    path('<slug:community_slug>/leave/', views.leave_community, name='leave_community'),
    path('<slug:community_slug>/', views.community_detail, name='community_detail'),
]