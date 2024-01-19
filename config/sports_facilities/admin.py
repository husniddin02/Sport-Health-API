from django.contrib import admin
from .models import SportsFacility

class SportsFacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_name', 'location', 'capacity', 'equipment_available', 'trainer_available')
    search_fields = ('facility_name', 'location')

admin.site.register(SportsFacility, SportsFacilityAdmin)
