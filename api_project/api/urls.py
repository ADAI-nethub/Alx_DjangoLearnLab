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

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # 🔐 Token login endpoint
    path('', include(router.urls)),
]

# Token authentication login endpoint
path('api-token-auth/', obtain_auth_token, name='api_token_auth')


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkshopViewSet, StoryViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('workshops', WorkshopViewSet)
router.register('stories', StoryViewSet)
router.register('users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import WorkshopListCreateView, StoryListCreateView, UserProfileRetrieveUpdateView

urlpatterns = [
    path('workshops/', WorkshopListCreateView.as_view(), name='workshop-list'),
    path('stories/', StoryListCreateView.as_view(), name='story-list'),
    path('profile/<int:pk>/', UserProfileRetrieveUpdateView.as_view(), name='userprofile-detail'),
]