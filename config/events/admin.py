from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'event_name', 'event_date', 'location', 'organizer')
    search_fields = ('user_profile__user__username', 'user_profile__user__email', 'event_name', 'organizer')
    filter_horizontal = ('facilities',)

admin.site.register(Event, EventAdmin)
