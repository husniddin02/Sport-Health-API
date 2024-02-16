from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_date', 'location', 'organizer']
    search_fields = ['event_name', 'location', 'organizer']
    list_filter = ['event_date']

admin.site.register(Event, EventAdmin)
