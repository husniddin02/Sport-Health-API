from django.contrib import admin
from .models import Health

class HealthAdmin(admin.ModelAdmin):
    list_display = ['user', 'height', 'weight', 'heart_rate', 'bmi_category']
    list_filter = ['user']
    search_fields = ['user__username']

admin.site.register(Health, HealthAdmin)
