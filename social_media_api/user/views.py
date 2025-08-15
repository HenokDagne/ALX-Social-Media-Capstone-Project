from django.shortcuts import render
from user.models import CustomUser
from user.serializers import CustomUserSerializer, UpdateProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework import generics
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
                    if not user.is_active:
                        return Response({"error": "User account is inactive."}, status=403)
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
    
    @action(detail=False, methods=['delete'], url_path='delete_account', permission_classes=[IsAuthenticated])
    def delete_account(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                username = user.username
                user.delete()
                return Response({"message": f"User {username} deleted successfully."})
            except Exception as e:
                return Response({"error": str(e)}, status=400)    
        return Response({"error": "User is not authenticated."}, status=403)
    
    @action(detail=False, methods=['get'], url_path='search_user', permission_classes=[IsAuthenticated])
    def search_user(self, request, username=None):
        username = request.query_params.get('username')
        if username:
            user = get_object_or_404(CustomUser, username=username)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return Response({"error": "Username is required."}, status=400)
    


# Move ProfileRetrieveUpdateView to top-level
class ProfileRetrieveUpdateView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow the authenticated user to retrieve/update their own profile
        return CustomUser.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        return self.request.user

