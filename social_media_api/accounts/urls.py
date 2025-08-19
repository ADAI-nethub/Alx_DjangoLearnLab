from django.urls import path
from .views import RegisterView, LoginView
from .views import follow_user, unfollow_user, user_profile, following_list, followers_list

urlpatterns = [
    # ... existing URLs ...
    
    # Follow management
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/<int:user_id>/follow/', follow_user, name='follow-user'),
    path('users/<int:user_id>/unfollow/', unfollow_user, name='unfollow-user'),
    path('users/<int:user_id>/profile/', user_profile, name='user-profile'),
    path('me/following/', following_list, name='following-list'),
    path('me/followers/', followers_list, name='followers-list'),
]


