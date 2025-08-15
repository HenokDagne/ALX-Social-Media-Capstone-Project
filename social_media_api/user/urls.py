
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import CustomUserViewSet, ProfileRetrieveUpdateView
router = DefaultRouter()
router.register(r'', CustomUserViewSet)
router.register(r'profile', ProfileRetrieveUpdateView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    
]