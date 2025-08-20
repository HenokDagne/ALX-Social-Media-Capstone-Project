from rest_framework import serializers
from user.models import CustomUser
from follow.models import Follow



class FollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.CharField(source='follower.username', read_only=True)
    following_username = serializers.CharField(source='following.username', read_only=True)

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at', 'follower_username', 'following_username']
        read_only_fields = ['id', 'created_at']
        