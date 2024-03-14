# serializers.py

from rest_framework import serializers
from .models import SportsFacility, FacilityDetails

class FacilityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityDetails
        fields = ['details_link']

class SportsFacilitySerializer(serializers.ModelSerializer):
    details = FacilityDetailsSerializer()

    class Meta:
        model = SportsFacility
        fields = ['facility_id', 'facility_name', 'location', 'capacity', 'equipment_available', 'trainer_available', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details', None)
        facility = SportsFacility.objects.create(**validated_data)
        if details_data:
            FacilityDetails.objects.create(facility=facility, **details_data)
        return facility

    def update(self, instance, validated_data):
        instance.facility_name = validated_data.get('facility_name', instance.facility_name)
        instance.location = validated_data.get('location', instance.location)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.equipment_available = validated_data.get('equipment_available', instance.equipment_available)
        instance.trainer_available = validated_data.get('trainer_available', instance.trainer_available)
        instance.save()

        details_data = validated_data.get('details', {})
        details = instance.details
        if details_data and details:
            details.details_link = details_data.get('details_link', details.details_link)
            details.save()

        return instance
