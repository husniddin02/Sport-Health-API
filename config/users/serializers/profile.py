# users/serializers/profile.py
from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "first_name", "last_name", "email", "is_superuser", "is_staff")
        read_only_fields = ("pk", "is_superuser", "is_staff")
