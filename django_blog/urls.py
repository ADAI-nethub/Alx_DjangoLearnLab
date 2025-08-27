from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Your blog app's views


urlpatterns = [
    # ... your existing URLs ...
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/new/', views.post_detail, name='comment_new'),  # Handled by post_detail
    path('post/<int:pk>/comment/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    path('post/<int:pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),

    # Home & About
    path('', views.home_view, name='blog-home'),
    path('about/', views.about_view, name='blog-about'),

    # User registration & profile
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # Authentication (custom templates)
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='blog/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='blog/logout.html'),
        name='logout'
    ),

    # Optional: password reset flow
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    # Blog posts (class-based views)
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
