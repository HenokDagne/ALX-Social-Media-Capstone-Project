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
    permission_classes = [AllowAny]
    serializer_class = FollowSerializer

    @action(detail=False, methods=['post', 'get'], url_path='following')
    def follow_user(self, request):
        user = request.user   # the logged-in user (follower)
        following_id = request.data.get('following_id')

        if not following_id:
            return Response(
                {"error": "Following ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Prevent self-following
        if str(user.id) == str(following_id):
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the user exists
        try:
            following = CustomUser.objects.get(id=following_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Create or get follow relation
        follow, created = Follow.objects.get_or_create(
            follower=user,
            following=following
        )

        if created:
            status_msg = "Now following"
            status_code = status.HTTP_201_CREATED
        else:
            status_msg = "Already following"
            status_code = status.HTTP_200_OK

        # Correct follower/following counts
        number_of_followers = following.followers.count()  # how many follow *this user*
        number_of_following = user.following.count()       # how many the logged-in user follows

        return Response({
            "status": status_msg,
            "follower": user.username,
            "following": following.username,
            "number_of_followers": number_of_followers,
            "number_of_following": number_of_following,
        }, status=status_code)

    @action(detail=False, methods=['delete'], url_path='unfollow')
    def unfollow_user(self, request):
        user = request.user  # the logged-in user (follower)
        following_id = request.data.get('following_id')

        if not following_id:
            return Response(
                {"error": "Following ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the user exists
        try:
            following = CustomUser.objects.get(id=following_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Delete follow relation
        follow = Follow.objects.filter(follower=user, following=following)
        if follow.exists():
            follow.delete()
            status_msg = "Unfollowed"
            status_code = status.HTTP_200_OK
        else:
            status_msg = "Not following"
            status_code = status.HTTP_400_BAD_REQUEST

        # Correct follower/following counts
        number_of_followers = following.followers.count()  # how many follow *this user*
        number_of_following = user.following.count()       # how many the logged-in user follows

        return Response({
            "status": status_msg,
            "follower": user.username,
            "following": following.username,
            "number_of_followers": number_of_followers,
            "number_of_following": number_of_following,
        }, status=status_code)
