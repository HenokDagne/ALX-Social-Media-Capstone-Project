from django.urls import path, include
from rest_framework import routers
from post.views import PostViewSet, PostFilterViewSet


router = routers.DefaultRouter()
router.register(r'post_data', PostViewSet)
router.register(r'post_filter', PostFilterViewSet, basename='post-filter')

urlpatterns = [
    path('', include(router.urls)),
]
