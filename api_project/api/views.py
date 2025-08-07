from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Story, UserProfile, Workshop
from .serializers import BookSerializer, StorySerializer, UserProfileSerializer, WorkshopSerializer

# ViewSets for complete CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.select_related('host').prefetch_related('stories')
    serializer_class = WorkshopSerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.select_related('author', 'workshop')
    serializer_class = StorySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.select_related('user')
    serializer_class = UserProfileSerializer

# Specialized generic views for custom endpoints
class PublishedBooksList(generics.ListAPIView):
    """List view for published books with custom filtering"""
    serializer_class = BookSerializer
    
    def get_queryset(self):
        return Book.objects.filter(published_date__isnull=False)

class WorkshopStoriesList(generics.ListCreateAPIView):
    """List/Create stories for a specific workshop"""
    serializer_class = StorySerializer
    
    def get_queryset(self):
        workshop_id = self.kwargs['workshop_id']
        return Story.objects.filter(workshop_id=workshop_id)
    
class BookList(generics.ListAPIView):
    """List view for all books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
