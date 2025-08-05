from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

class BookListView(generics.ListAPIView):
    """
    API endpoint that allows books to be viewed.
    
    Permissions:
    - All users (authenticated or not) can view the list
    
    Methods:
    - GET: Returns a list of all books
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
        })

class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving a single book
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
    API endpoint for creating new books
    
    Permissions:
    - Only authenticated users can create books
    - Owner is automatically set to the requesting user
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
        return Response(
            {
                "status": "success",
                "message": "Book created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class BookUpdateView(generics.RetrieveUpdateAPIView):
    """
    API endpoint for updating books
    
    Permissions:
    - Only authenticated owners can update books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {
                "status": "success",
                "message": "Book updated successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

class BookDeleteView(generics.DestroyAPIView):
    """
    API endpoint for deleting books
    
    Permissions:
    - Only authenticated owners can delete books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "status": "success",
                "message": "Book deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )
    
    