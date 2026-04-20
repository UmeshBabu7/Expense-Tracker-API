from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "bio",
            "is_superuser",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "is_superuser"]
