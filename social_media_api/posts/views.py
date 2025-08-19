from rest_framework import viewsets, permissions, filters, generics
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from accounts.models import User
from notifications.models import Notification
from django_filters.rest_framework import DjangoFilterBackend

# Permission class for object-level access
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# ViewSet for Posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # ✅ explicit

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])  # ✅ explicit
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({'status': 'post liked'})
        return Response({'status': 'already liked'}, status=400)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])  # ✅ explicit
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'post unliked'})
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=400)


# API view for user feed
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])  # ✅ explicit
def user_feed(request):
    followed_users = request.user.following.all()
    feed_posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(feed_posts, 10)
    try:
        posts_page = paginator.page(page)
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages)
    
    serializer = PostSerializer(posts_page, many=True, context={'request': request})
    return Response({
        'posts': serializer.data,
        'has_next': posts_page.has_next(),
        'has_previous': posts_page.has_previous(),
        'current_page': posts_page.number,
        'total_pages': paginator.num_pages
    })


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_id).order_by('created_at')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)
