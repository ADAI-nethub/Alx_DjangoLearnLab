"""
URL configuration for blog application.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    home_view,
    about_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    profile_view,
)

app_name = 'blog'

urlpatterns = [
    # Home & About
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),

    # Post operations
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Authentication (custom views)
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),

    # Authentication (built-in views)
    path('login/',
         auth_views.LoginView.as_view(
             template_name='registration/login.html',
             redirect_authenticated_user=True
         ),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='registration/logout.html',
             next_page='home'
         ),
         name='logout'),

    # Admin
    path('admin/', admin.site.urls),

    # Optional accounts app
    path('accounts/', include('accounts.urls')),
]

# Error handlers
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
