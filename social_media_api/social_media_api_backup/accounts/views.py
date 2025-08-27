
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Use CustomUser via get_user_model
CustomUser = get_user_model()

class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # ✅ uses CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # public endpoint

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user_id": user.id,
            "email": user.email
        })


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
            'email': user.email
        })
