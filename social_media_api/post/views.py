from django.shortcuts import render
from post.serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from post.models import Post
from post.filter import PostFilter
from rest_framework import filters
from django.shortcuts import get_object_or_404
from comment.models import Comment
from comment.serializers import CommentSerializer, CommentWithPostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostFilterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = [
        '^title',         # Starts-with search for title
        '=user__email',   # Exact match for user email
        '$title',         # Regex search for title
        'content',        # Default contains search for content
        'user__username', # Search by username (contains by default)
    ]

    @action(detail=False, methods=['get'], url_path='comment_post')
    def comment_related_post(self, request):
        post = request.query_params.get('post_id')
        if post:
            try:
                post_instance = get_object_or_404(Post, id=post)
                comment = Comment.objects.filter(post=post_instance)
                serializer = CommentWithPostSerializer(comment, many=True)
                return Response(serializer.data, status=200)
            except Comment.DoesNotExist:
                return Response({"error": "No comments found for this post."}, status=404)

        return Response({"error": "Post ID is required."}, status=400)




    

    


    
