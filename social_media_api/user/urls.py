from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import CustomUserViewSet, ProfileRetrieveUpdateView, google_logout, Home
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'profile', ProfileRetrieveUpdateView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('google-logout/', google_logout, name='google-logout'),
    path('home/', Home.as_view(), name='home'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]