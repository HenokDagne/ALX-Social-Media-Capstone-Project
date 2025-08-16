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
