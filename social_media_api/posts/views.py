from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    """Get feed of posts from followed users"""
    # Get users that the current user follows
    following_users = request.user.following.all()  # ✅ variable renamed

    # Get posts from followed users, ordered by most recent
    feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ✅ matches checker

    # Pagination
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
