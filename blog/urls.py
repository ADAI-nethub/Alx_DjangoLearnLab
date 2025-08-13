"""
URL configuration for blog application

Defines all URL patterns for:
- Core pages (home, about)
- Post CRUD operations
- User authentication
- Admin interface
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    home,
    about,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    profile_view,
    handler404,
    handler500
)

app_name = 'blog'

urlpatterns = [
    # Core pages
    path('', home, name='home'),
    path('about/', about, name='about'),
    
    # Post operations
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
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
    
    # Accounts app (if you have separate accounts app)
    path('accounts/', include('accounts.urls')),
]

# Error handlers
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'