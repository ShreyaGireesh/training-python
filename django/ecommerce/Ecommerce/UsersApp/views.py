from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

CustomUser = get_user_model()

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_role(request):
    return Response({"role": request.user.role, "name": request.user.name, "userid":request.user.id})

class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_description="Create a new user (customer or seller)",
        request_body=CustomUserSerializer,
        responses={201: CustomUserSerializer, 400: "Bad Request"},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "pk" 
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_description="Update an existing user",
        request_body=CustomUserSerializer,
        responses={200: CustomUserSerializer, 400: "Bad Request", 404: "Not Found"},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "refresh": openapi.Schema(type=openapi.TYPE_STRING, description="Refresh Token"),
            },
            required=["refresh"],
        ),
        responses={200: "Successfully logged out", 400: "Invalid token"},
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


def test_error(request):
    print("🚨 Raising a test error!")
    raise ValueError("Testing error handling!")