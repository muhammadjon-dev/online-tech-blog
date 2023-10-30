from django.urls import path
from .views import *
from django.contrib.auth import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('change-account/', UserEditAccountView.as_view(), name='change_account'),
    path('password/', UserChangePasswordView.as_view(), name='password'),
    path('profile/<str:username>/', UserShowProfileView.as_view(), name='profile'),
    path('profile-edit/<str:username>/', UserEditProfile.as_view(), name='profile_edit'),
    path('reset_password/', UserResetPasswordView.as_view(), name='reset_password'),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
]