# sportFacilities/serializers.py
from rest_framework import serializers
from .models import SportsFacility

class SportsFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsFacility
        fields = ['facility_id', 'facility_name', 'location', 'capacity', 'equipment_available', 'trainer_available']
