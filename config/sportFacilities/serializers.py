from rest_framework import serializers
from .models import SportsFacility

class SportsFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsFacility
        fields = ['facility_id', 'facility_name', 'location', 'capacity', 'equipment_available', 'trainer_available']

    def create(self, validated_data):
        return SportsFacility.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.facility_name = validated_data.get('facility_name', instance.facility_name)
        instance.location = validated_data.get('location', instance.location)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.equipment_available = validated_data.get('equipment_available', instance.equipment_available)
        instance.trainer_available = validated_data.get('trainer_available', instance.trainer_available)
        instance.save()
        return instance
