
from django.urls import path, include
from comment.views import CommentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    
]