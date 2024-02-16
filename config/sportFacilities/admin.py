from django.contrib import admin
from .models import SportsFacility

@admin.register(SportsFacility)
class SportsFacilityAdmin(admin.ModelAdmin):
    list_display = ['facility_name', 'location', 'capacity', 'equipment_available', 'trainer_available']
    list_filter = ['location', 'capacity', 'equipment_available', 'trainer_available']
    search_fields = ['facility_name', 'location']
