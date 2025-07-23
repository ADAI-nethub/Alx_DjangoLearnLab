"""
Security Documentation - views.py

✔ Uses Django ORM to avoid SQL injection.
✔ Validates all user input using Django Forms (BookForm, ExampleForm).
✔ Applies fine-grained permission controls using @permission_required decorators.
✔ All POST requests include {% csrf_token %} to protect against CSRF.
✔ Delete views use POST method only with confirmation step to prevent accidental deletions.

For more information, see Django security practices: https://docs.djangoproject.com/en/stable/topics/security/
"""

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, ExampleForm  # ✅ Import ExampleForm for secure input handling


# 📘 Secure book creation with validation and permissions
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# 🔍 Book list view + optional secure search with ExampleForm
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    form = ExampleForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = books.filter(title__icontains=query)  # safe ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

# ✏️ Edit book securely
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {'form': form})

# ❌ Delete book with confirmation
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})
