from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post  # Make sure you have this model

# Add this home view function
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

# Your existing class-based views...
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Or your template
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


def register_view(request):
    """
    Handles user registration with success message and auto-login
    """
    if request.user.is_authenticated:
        return redirect('blog-home')  # Redirect if already logged in

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Auto-login after registration
            login(request, user)
            messages.success(request, f'Account created for {username}! You are now logged in.')
            return redirect('profile')  # Redirect to profile after registration
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    """
    Custom login view with remember me functionality
    """
    if request.user.is_authenticated:
        return redirect('blog-home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if not remember_me:
                # Set session to expire when browser closes
                request.session.set_expiry(0)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('blog-home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

@login_required
def logout_view(request):
    """
    Handles user logout with confirmation message
    """
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('blog-home')

@login_required
def profile_view(request):
    """
    Handles both profile viewing and updating
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  # POST-REDIRECT-GET pattern

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)