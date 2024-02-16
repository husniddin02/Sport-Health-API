# health/serializers.py
from rest_framework import serializers
from .models import Health

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ['health_id', 'user_id', 'height', 'weight', 'heart_rate', 'bmi', 'bmi_category', 'additional_notes']
