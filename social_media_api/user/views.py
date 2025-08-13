from django.shortcuts import render
from user.models import CustomUser
from user.serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['post'], url_path='signup')
    def signup(self, request):
        last_name = request.data.get('last_name')
        first_name = request.data.get('first_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if last_name and first_name and username and email and password:
            try:
                user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
                )
                refresh = RefreshToken.for_user(user)
                serializer = self.get_serializer(user)
                return Response({
                    "user": serializer.data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }, status=200)
            except Exception as e:
                return Response({"error": str(e)}, status=400)

        return Response({"error": "All fields are required."}, status=400)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email and password:
            username = CustomUser.objects.get(email=email).username
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    refresh = RefreshToken.for_user(user)
                    serializer = self.get_serializer(user)
                    return Response({
                        "user": serializer.data,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    })
                else:
                    return Response({"error": "Invalid credentials."}, status=400)
            except CustomUser.DoesNotExist:
                return Response({"error": "User not found."}, status=404)

        return Response({"error": "Email and password are required."}, status=400)
