# advanced_api_project/api/views.py

from rest_framework import generics, filters # Importing filters from rest_framework.filters
from rest_framework.filters import SearchFilter, OrderingFilter

# This is the line that makes the statement "false".
# It is incorrect and will likely cause an ImportError.
from django_filters import rest_framework 
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer

# ... the rest of  view classes would follow
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, filters.OrderingFilter] # The additional change is here
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving a single book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    API view for creating a new book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    """
    API view for updating an existing book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    """
    API view for deleting an existing book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer