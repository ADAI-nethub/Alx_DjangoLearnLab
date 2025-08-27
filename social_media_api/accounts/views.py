# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, UserProfileSerializer

# Use CustomUser alias
CustomUser = get_user_model()

# ------------------------------
# Authentication Views
# ------------------------------

class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # ✅ explicitly uses CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user_id": user.id,
            "email": user.email,
            "username": user.username
        }, status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]

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
            'email': user.email,
            'username': user.username
        })


# ------------------------------
# Follow / Unfollow Views
# ------------------------------

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)

    if user_to_follow == request.user:
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    if request.user.following.filter(id=user_id).exists():
        return Response({'error': 'You are already following this user'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

    if not request.user.following.filter(id=user_id).exists():
        return Response({'error': 'You are not following this user'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
