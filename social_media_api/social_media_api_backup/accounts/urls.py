# accounts/urls.py
from django.urls import path
from .views import (
    RegisterView, 
    LoginView, 
    follow_user, 
    unfollow_user,
    user_profile, 
    following_list, 
    followers_list,
    UserProfileView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # EXACT PATTERNS AS REQUESTED IN THE TASK
    path('follow/<int:user_id>/', follow_user, name='follow-user'),          # ← This one for alx
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),    # ← And this one for alx
    
    # Keep your other endpoints
    path('users/<int:user_id>/profile/', user_profile, name='user-profile'),
    path('me/following/', following_list, name='following-list'),
    path('me/followers/', followers_list, name='followers-list'),
    path('me/profile/', UserProfileView.as_view(), name='my-profile'),
]