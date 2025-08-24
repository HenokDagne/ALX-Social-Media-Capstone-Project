from django.urls import path, include
from rest_framework import routers
from post.views import PostViewSet, PostFilterViewSet, LikeViewSet


router = routers.DefaultRouter()
router.register(r'post_data', PostViewSet)
router.register(r'post_filter', PostFilterViewSet, basename='post-filter')
router.register(r'', LikeViewSet, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
]
