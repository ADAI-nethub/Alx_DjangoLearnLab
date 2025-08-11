# bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,  # Use False if search is optional
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )


