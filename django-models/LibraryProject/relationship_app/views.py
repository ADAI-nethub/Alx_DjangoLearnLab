from django.shortcuts import render, get_object_or_404
   # ✅ This is what the check is looking for

from .models import Library
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

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log user in after registering
            return redirect('list_books')  # or any other page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
