from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import CustomUserViewSet, ProfileRetrieveUpdateView, google_logout, Home

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'profile', ProfileRetrieveUpdateView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('google-logout/', google_logout, name='google-logout'),
    path('home/', Home.as_view(), name='home'),
]