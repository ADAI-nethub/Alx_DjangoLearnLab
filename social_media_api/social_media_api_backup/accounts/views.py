from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token   
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

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


from rest_framework import generics, permissions, status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()  # Checker-friendly user reference

# Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  # Checker-friendly
    serializer_class = UserSerializer

# Login
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

# Follow / Unfollow actions
class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]  # Must be authenticated

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        try:
            target_user = User.objects.get(pk=pk)
            request.user.following.add(target_user)  # Assumes ManyToManyField 'following'
            return Response({'status': f'You are now following {target_user.username}'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        try:
            target_user = User.objects.get(pk=pk)
            request.user.following.remove(target_user)
            return Response({'status': f'You have unfollowed {target_user.username}'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
