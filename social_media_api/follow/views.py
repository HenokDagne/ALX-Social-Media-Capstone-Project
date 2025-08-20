from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from .models import Follow
from .serializers import FollowSerializer
from user.models import CustomUser


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'], url_path='follow_user')
    def follow_user(self, request):
        user = request.user
        following_id = request.data.get('following_id')
        
        if not following_id:
            return Response({"error": "following_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.id == int(following_id):
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            following = CustomUser.objects.get(id=following_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        follow, created = Follow.objects.get_or_create(follower=user, following=following)

        if created:
            return Response({"status": f"Now following {following.username}"}, status=status.HTTP_201_CREATED)
        
        return Response({"status": f"You are already following {following.username}"}, status=status.HTTP_200_OK)
    @action(detail=False, methods=['post', 'delete'], url_path="unfollow")
    def unfollow_user(self, request):
        user = request.user # logged-in user = follower
        following_id = request.data.get("following_id")

        if not following_id:
            return Response({"error": "following_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            follow = Follow.objects.get(follower=user, following_id=following_id)
            follow.delete()
            return Response({"status": "Unfollowed successfully"}, status=status.HTTP_200_OK)
        except Follow.DoesNotExist:
            return Response({"error": "You are not following this user"}, status=status.HTTP_404_NOT_FOUND)
        
    # list my followers
    @action(detail=False, methods=["get"], url_path="followers")
    def get_followers(self, request):
        user = request.user
        followers = user.followers.all()
        serializer = self.get_serializer(followers, many=True)
        return Response(serializer.data)
    # list who I am following
    @action(detail=False, methods=["get"], url_path="following")
    def get_following(self, request):
        user = request.user
        following = user.following.all()
        serializer = self.get_serializer(following, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'], url_path="count_follow")
    def get_following_and_followers_numbers(self, request):
        user = request.user
        followers_numbers = user.followers.count()
        following_numbers = user.following.count()
        return Response({
            "followers": followers_numbers,
            "following": following_numbers
        })
