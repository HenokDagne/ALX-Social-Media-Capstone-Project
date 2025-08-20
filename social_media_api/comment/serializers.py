from rest_framework import serializers
from user.models import CustomUser
from post.models import Post
from comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())


    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']
        read_only_fields = ['created_at', 'user', 'post']


class CommentWithPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Comment
        fields = ['post_title', 'username', 'content', 'created_at']
        read_only_fields = ['created_at', 'username', 'post_title']
