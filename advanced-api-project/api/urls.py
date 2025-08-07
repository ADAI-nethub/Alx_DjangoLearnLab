from .views import DefaultBookUpdateView
from rest_framework.schemas import get_schema_view
from api.views import BookUpdateView
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)
from .views import (
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView,
    DefaultBookUpdateView, DefaultBookDeleteView  # Add this import
)


schema_view = get_schema_view(
    title="Book API",
    description="API for filtering, searching and ordering books",
)


    

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Optional default views for testing or fallback (without PK)
    path('books/update/', DefaultBookUpdateView.as_view(), name='book-update-no-pk'),
    path('books/delete/', DefaultBookDeleteView.as_view(), name='book-delete-no-pk'),
]


from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

