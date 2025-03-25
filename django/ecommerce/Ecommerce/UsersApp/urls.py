from django.urls import path
from .views import UserCreateAPIView, UserUpdateAPIView, LogoutView, get_user_role, test_error
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("add/", UserCreateAPIView.as_view(), name="add_user"),  # API to add a user
    path("edit/<int:pk>/", UserUpdateAPIView.as_view(), name="edit_user"),  # API to edit a user
    path("user-role/", get_user_role, name="user_role"),

    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("test-error/", test_error, name="test_error"),
]