from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

# ✅ Secure user input form for demonstration
class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=True,
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )
