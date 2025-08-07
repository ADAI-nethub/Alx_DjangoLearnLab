from rest_framework import generics, status, permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import BookFilter  # Custom filter class



# ----------------------------
# Book List & Search View
# ----------------------------
class BookListView(generics.ListAPIView):
    """
    GET: List all books with filtering, searching, and ordering.
    - Publicly accessible.
    - Supports:
        - Filtering: Via `BookFilter` (e.g., `?author__name=John`).
        - Search: Partial matches in `title`, `author__name`, `publication_year` (e.g., `?search=Python`).
        - Ordering: By `title`, `publication_year`, etc. (e.g., `?ordering=-publication_year`).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name', 'publication_year']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']  # Default order

    def list(self, request, *args, **kwargs):
        """Enhanced response with metadata about filters/search."""
        response = super().list(request, *args, **kwargs)
        return Response({
            "status": "success",
            "count": len(response.data),
            "filters": {
                "available": {
                    "filter_by": list(self.filterset_class.get_fields().keys()),
                    "search_in": self.search_fields,
                    "order_by": self.ordering_fields,
                },
                "applied": {
                    "filters": request.query_params,
                    "search": request.query_params.get('search'),
                    "ordering": request.query_params.get('ordering'),
                }
            },
            "data": response.data
        }, status=status.HTTP_200_OK)

# ----------------------------
# Book Create View
# ----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    - Requires authentication.
    - Automatically sets the `owner` to the current user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        """Custom response format."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": "success",
            "message": "Book created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

# ----------------------------
# Book Detail/Update/Delete Views
# ----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book's details.
    - Publicly accessible.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookUpdateView(generics.RetrieveUpdateAPIView):
    """
    PUT/PATCH: Update a book.
    - Requires authentication + ownership (via `IsOwnerOrReadOnly`).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        """Custom response format."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "status": "success",
            "message": "Book updated successfully",
            "data": serializer.data
        })

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Delete a book.
    - Requires authentication + ownership (via `IsOwnerOrReadOnly`).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

# ----------------------------
# Default Book Actions (Demo/Testing)
# ----------------------------
class DefaultBookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Delete the first available book (for testing).
    - Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        book = Book.objects.first()
        if not book:
            raise Book.DoesNotExist("No books available to delete.")
        return book

class DefaultBookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update the first available book (for testing).
    - Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        book = Book.objects.first()
        if not book:
            raise Book.DoesNotExist("No books available to update.")
        return book