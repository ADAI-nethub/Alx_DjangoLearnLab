<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    # ✅ include posts.urls under /api/
    path('api/', include('posts.urls')),
=======
# social_media_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/notifications/', include('notifications.urls')),
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/", include("posts.urls")),
>>>>>>> 9c7079d203d65aff9c534a66e4acb655035b7684
]
