from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('user_list/', views.UserListAPIView.as_view()),
    path('user_detail/<int:pk>/', views.UserDetailAPIView.as_view()),
    path('register/',views.UserCreateAPIView.as_view()),
    path('user_update/<int:pk>/', views.UserUpdateAPIView.as_view()),
    path('user_delete/<int:pk>/', views.UserDestroyAPIView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
    