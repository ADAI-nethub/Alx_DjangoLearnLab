# advanced_api_project/api/urls.py

from django.urls import path
from rest_framework.schemas import get_schema_view

# Import only the views that are actually defined in your views.py file.
# This single, clean import statement prevents clutter and errors.
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

# You can keep your schema view configuration
schema_view = get_schema_view(
    title="Book API",
    description="API for filtering, searching, and ordering books",
)

urlpatterns = [
    # API endpoints for your books
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    
    # You can also add the schema path if you want to
    path('schema/', schema_view, name='api-schema'),
]