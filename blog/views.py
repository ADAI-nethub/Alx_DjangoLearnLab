from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib.auth import views as auth_views

# URLs example (in blog/urls.py)
path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='post-list'), name='logout'),


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # default: <app>/<model>_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # default: <app>/<model>_detail.html

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect('profile')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Update user email and optionally more fields
        email = request.POST.get('email')
        if email:
            request.user.email = email
            request.user.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, 'Please provide a valid email.')
    return render(request, 'registration/profile.html')
