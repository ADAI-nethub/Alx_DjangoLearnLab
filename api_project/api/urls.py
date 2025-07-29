from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
# urls.py
from .views import BookList, BookDetail, BookCreate

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/create/', BookCreate.as_view(), name='book-create'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet  # Ensure both are imported

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: This keeps your ListAPIView separately available
    path('books/', BookList.as_view(), name='book-list'),

    # Include all auto-generated ViewSet routes
    path('', include(router.urls)),
]
