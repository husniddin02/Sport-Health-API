# workouts/models.py
from django.db import models
from users.models import User

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор тренировки")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    workout_date = models.DateField(verbose_name="Дата тренировки")
    exercise_type = models.CharField(max_length=100, verbose_name="Тип упражнения")
    duration = models.DurationField(verbose_name="Продолжительность тренировки")
    notes = models.TextField(null=True, blank=True, verbose_name="Заметки")

    def __str__(self):
        return f"Запись о тренировке пользователя {self.user.username} от {self.workout_date}"

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"
