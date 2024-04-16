from django.test import TestCase
from .models import Workout
from users.models import User
from datetime import timedelta

class WorkoutModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем пользователя
        cls.user = User.objects.create_user(username='test', email='test@example.com', password='password')

        # Создаем тренировку
        cls.workout = Workout.objects.create(
            user=cls.user,
            workout_date='2022-01-01',
            exercise_type='Running',
            duration=timedelta(minutes=30),
            notes='A good workout'
        )

    def test_user_username(self):
        """Тестирование поля пользователя по имени пользователя."""
        workout = Workout.objects.get(pk=self.workout.pk)
        self.assertEqual(workout.user.username, 'test')

    def test_workout_string_representation(self):
        """Тестирование строкового представления тренировки."""
        workout = Workout.objects.get(pk=self.workout.pk)
        expected_str = f"Запись о тренировке пользователя test от 2022-01-01"
        self.assertEqual(str(workout), expected_str)
