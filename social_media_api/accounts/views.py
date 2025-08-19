# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import User
from .serializers import UserSerializer, UserProfileSerializer

User = get_user_model()

# Existing views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })

# NEW: Add the follow/unfollow functions HERE
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    """Follow another user"""
    user_to_follow = get_object_or_404(User, id=user_id)
    
    if user_to_follow == request.user:
        return Response(
            {'error': 'You cannot follow yourself'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.user.following.filter(id=user_id).exists():
        return Response(
            {'error': 'You are already following this user'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.add(user_to_follow)
    return Response(
        {'message': f'You are now following {user_to_follow.username}'},
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    """Unfollow a user"""
    user_to_unfollow = get_object_or_404(User, id=user_id)
    
    if not request.user.following.filter(id=user_id).exists():
        return Response(
            {'error': 'You are not following this user'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.remove(user_to_unfollow)
    return Response(
        {'message': f'You have unfollowed {user_to_unfollow.username}'},
        status=status.HTTP_200_OK
    )

# You can add more views below...