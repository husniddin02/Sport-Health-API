from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_id', 'event_name', 'event_date', 'location', 'description', 'organizer']

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.location = validated_data.get('location', instance.location)
        instance.description = validated_data.get('description', instance.description)
        instance.organizer = validated_data.get('organizer', instance.organizer)
        instance.save()
        return instance
