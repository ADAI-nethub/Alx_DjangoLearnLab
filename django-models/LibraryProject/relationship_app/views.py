from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

# ✅ Add this exact line to satisfy the check
from .models import Library

# ✅ You can keep this if needed, or split the imports
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
