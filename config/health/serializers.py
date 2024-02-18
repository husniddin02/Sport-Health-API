from rest_framework import serializers
from .models import Health

class HealthSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Health.
    """

    class Meta:
        model = Health
        fields = ['health_id', 'user', 'height', 'weight', 'heart_rate', 'bmi', 'bmi_category', 'additional_notes']

    def create(self, validated_data):
        return Health.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.heart_rate = validated_data.get('heart_rate', instance.heart_rate)
        instance.bmi = validated_data.get('bmi', instance.bmi)
        instance.bmi_category = validated_data.get('bmi_category', instance.bmi_category)
        instance.additional_notes = validated_data.get('additional_notes', instance.additional_notes)
        instance.save()
        return instance
