from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token   
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    """Follow another user"""
    user_to_follow = get_object_or_404(User, id=user_id)
    
    if user_to_follow == request.user:
        return Response(
            {'error': 'You cannot follow yourself'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.user.follow(user_to_follow):
        return Response(
            {'message': f'You are now following {user_to_follow.username}'},
            status=status.HTTP_200_OK
        )
    
    return Response(
        {'error': 'You are already following this user'},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    """Unfollow a user"""
    user_to_unfollow = get_object_or_404(User, id=user_id)
    
    if request.user.unfollow(user_to_unfollow):
        return Response(
            {'message': f'You have unfollowed {user_to_unfollow.username}'},
            status=status.HTTP_200_OK
        )
    
    return Response(
        {'error': 'You are not following this user'},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request, user_id):
    """Get user profile with follow status"""
    user = get_object_or_404(User, id=user_id)
    serializer = UserProfileSerializer(user, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def following_list(request):
    """Get list of users the current user is following"""
    following = request.user.following.all()
    serializer = UserProfileSerializer(following, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followers_list(request):
    """Get list of users following the current user"""
    followers = request.user.followers.all()
    serializer = UserProfileSerializer(followers, many=True, context={'request': request})
    return Response(serializer.data)


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
