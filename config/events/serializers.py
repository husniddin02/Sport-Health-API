from rest_framework import serializers
from .models import Event, EventDetails

class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = ['details_link']

class EventSerializer(serializers.ModelSerializer):
    details = EventDetailsSerializer()

    class Meta:
        model = Event
        fields = ['event_id', 'event_name', 'location', 'event_date', 'organizer', 'description', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        event = Event.objects.create(**validated_data)
        EventDetails.objects.create(event=event, **details_data)
        return event

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', {})
        details, _ = EventDetails.objects.get_or_create(event=instance)
        
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.location = validated_data.get('location', instance.location)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.organizer = validated_data.get('organizer', instance.organizer)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        details.details_link = details_data.get('details_link', details.details_link)
        details.save()

        return instance
