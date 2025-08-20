
from django.urls import path, include
from .views import FollowViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    
]