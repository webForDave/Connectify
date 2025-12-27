from dj_rest_auth.views import LoginView, UserDetailsView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('users/me/', UserDetailsView.as_view(), name='user_details'),
    path('users/<str:username>/', views.user_detials, name='user_details'),
]
