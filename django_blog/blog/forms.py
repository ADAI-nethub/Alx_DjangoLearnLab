from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment

from django import forms
from .models import Post
# If using manual tags:
from .models import Tag

class PostForm(forms.ModelForm):
    # For django-taggit:
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")
    
    # For manual tags:
    # tag_names = forms.CharField(required=False, help_text="Enter tags separated by commas")
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include all your fields


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
