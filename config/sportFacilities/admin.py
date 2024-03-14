# admin.py

from django.contrib import admin
from .models import SportsFacility, FacilityDetails

@admin.register(SportsFacility)
class SportsFacilityAdmin(admin.ModelAdmin):
    list_display = ['facility_name', 'location', 'capacity', 'equipment_available', 'trainer_available']
    list_filter = ['location', 'capacity', 'equipment_available', 'trainer_available']
    search_fields = ['facility_name', 'location']

@admin.register(FacilityDetails)
class FacilityDetailsAdmin(admin.ModelAdmin):
    list_display = ['facility', 'details_link']
