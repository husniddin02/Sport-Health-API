from django.contrib import admin
from .models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'workout_date', 'exercise_type', 'duration')
    search_fields = ('user_profile__user__username', 'user_profile__user__email', 'exercise_type')

admin.site.register(Workout, WorkoutAdmin)
