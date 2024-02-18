from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['workout_id', 'user', 'workout_date', 'exercise_type', 'duration', 'notes']

    def create(self, validated_data):
        return Workout.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.workout_date = validated_data.get('workout_date', instance.workout_date)
        instance.exercise_type = validated_data.get('exercise_type', instance.exercise_type)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance
