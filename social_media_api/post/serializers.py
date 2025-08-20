from rest_framework import serializers
from user.models import CustomUser
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'create_at', 'updated_at', 'user', 'image']
        read_only_fields = ['create_at', 'updated_at', 'user']


    
