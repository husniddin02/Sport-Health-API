from django.contrib import admin
from .models import Event, EventDetails

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_date', 'location', 'organizer']
    list_filter = ['event_date', 'location']
    search_fields = ['event_name', 'location', 'organizer']
    ordering = ['event_date']

@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ['event', 'details_link']
    search_fields = ['event__event_name', 'details_link']
