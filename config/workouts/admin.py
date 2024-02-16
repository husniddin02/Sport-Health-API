from django.contrib import admin
from .models import Workout

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'workout_date', 'exercise_type', 'duration']
    list_filter = ['user', 'workout_date', 'exercise_type']
    search_fields = ['user__username', 'exercise_type', 'notes']
