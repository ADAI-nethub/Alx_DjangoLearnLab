"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Main URL patterns
urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Blog app URLs (delegated to blog/urls.py)
    path('', include('blog.urls')),
    
    # Authentication URLs (can be included from django.contrib.auth if using default auth views)
    path('accounts/', include('django.contrib.auth.urls')),
]

# Media files in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)