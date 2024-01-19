from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class CustomUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'blood_pressure', 'heart_rate', 'date_of_birth', 'gender', 'address', 'profile_photo')
    search_fields = ('user__username', 'user__email')

admin.site.register(UserProfile, CustomUserProfileAdmin)
