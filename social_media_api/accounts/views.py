# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model  # Use this instead of CustomUser.objects

# Import your models and serializers
from .models import User  # Assuming your custom user model is named User
from .serializers import UserSerializer, UserProfileSerializer

# Get the user model - this is the correct way
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    View for user registration
    """
    queryset = User.objects.all()  # Use User.objects instead of CustomUser.objects
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

class LoginView(ObtainAuthToken):
    """
    View for user login - returns token
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })

# Function-based views for follow functionality
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Use permissions.IsAuthenticated
def follow_user(request, user_id):
    """Follow another user"""
    user_to_follow = get_object_or_404(User, id=user_id)
    
    if user_to_follow == request.user:
        return Response(
            {'error': 'You cannot follow yourself'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Check if already following
    if request.user.following.filter(id=user_id).exists():
        return Response(
            {'error': 'You are already following this user'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Add to following
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
    
    # Check if actually following
    if not request.user.following.filter(id=user_id).exists():
        return Response(
            {'error': 'You are not following this user'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Remove from following
    request.user.following.remove(user_to_unfollow)
    return Response(
        {'message': f'You have unfollowed {user_to_unfollow.username}'},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_profile(request, user_id):
    """Get user profile with follow status"""
    user = get_object_or_404(User, id=user_id)
    serializer = UserProfileSerializer(user, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def following_list(request):
    """Get list of users the current user is following"""
    following = request.user.following.all()
    serializer = UserProfileSerializer(following, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def followers_list(request):
    """Get list of users following the current user"""
    followers = request.user.followers.all()
    serializer = UserProfileSerializer(followers, many=True, context={'request': request})
    return Response(serializer.data)

# Additional view for user profile management
class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    View to retrieve and update user profile
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user