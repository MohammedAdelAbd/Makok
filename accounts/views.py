from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import *
from .serializers import *
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:

            token = AuthToken.objects.create(user)[1]
            return Response(
                {
                    "message": "Login successful",
                    "user": user.email,
                    "token": token},
                status=status.HTTP_200_OK
            )
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate a token for the newly registered user
        token = AuthToken.objects.create(user)[1]

        return Response({
            "message": "User registered successfully",
            "user": user.email,
            "token": token
        }, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        print(queryset)
        return Response(serializer.data)
