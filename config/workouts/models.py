from django.db import models
from users.models import UserProfile

class Workout(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Профиль пользователя")
    workout_date = models.DateField("Дата тренировки")
    exercise_type = models.CharField("Тип упражнения", max_length=50)
    duration = models.DurationField("Продолжительность тренировки")
    notes = models.TextField("Дополнительные заметки о тренировке", null=True, blank=True)

    def __str__(self):
        return f"Тренировка {self.user_profile.user.username} - {self.workout_date}"

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"
