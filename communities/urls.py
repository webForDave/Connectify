from . import views
from django.urls import path

urlpatterns = [
    path('', views.communities, name='communities'),
    path('<slug:community_slug>/', views.community, name='community_detail'),
    path('<slug:community_slug>/join/', views.join_community, name='join_community'),
    path('<slug:community_slug>/leave/', views.leave_community, name='leave_community'),
]