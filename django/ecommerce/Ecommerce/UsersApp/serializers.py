from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ["id", "email", "name","password", "role", "business_license"]
    
    def create(self, validated_data):
        """Create a new user using the CustomUserManager."""
        return CustomUser.objects.create_user(**validated_data)