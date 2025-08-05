from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly


class BookListView(generics.ListAPIView):
    """
    GET: List all books (accessible to everyone)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            "status": "success",
            "count": len(response.data),
            "data": response.data
        }, status=status.HTTP_200_OK)


class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book (accessible to everyone)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "status": "success",
            "data": serializer.data
        })


class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "status": "success",
            "message": "Book created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)


class BookUpdateView(generics.RetrieveUpdateAPIView):
    """
    PUT/PATCH: Update an existing book (only owner, authenticated)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
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
    DELETE: Remove a book (only owner, authenticated)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
