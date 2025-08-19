from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login at accounts/login/
    # OR for custom path:
    path('login/', 
         auth_views.LoginView.as_view(
             template_name='registration/login.html'  # This is what you need to verify
         ),
         name='login'),
    path('', include('blog.urls')),
]