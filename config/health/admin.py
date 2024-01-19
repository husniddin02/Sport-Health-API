from django.contrib import admin
from .models import Health

class HealthAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'height', 'weight', 'heart_rate', 'bmi', 'bmi_category')
    search_fields = ('user_profile__user__username', 'user_profile__user__email')

admin.site.register(Health, HealthAdmin)
