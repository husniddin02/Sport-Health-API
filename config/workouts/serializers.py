# workouts/serializers.py
from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['workout_id', 'user_id', 'workout_date', 'exercise_type', 'duration', 'notes']
