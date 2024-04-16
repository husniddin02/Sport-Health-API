# health/models.py

from django.db import models
from users.models import User

class Health(models.Model):
    health_id = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор записи о здоровье")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", default=1)

    # Physical measurements
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Рост (см)")
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Вес (кг)")

    # Vital signs
    heart_rate = models.IntegerField(null=True, blank=True, verbose_name="Частота сердечных сокращений (уд./мин.)")

    # Body mass index (BMI)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Индекс массы тела (ИМТ)")
    bmi_category = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('underweight', 'Ниже нормального веса'),
        ('normal', 'Нормальный вес'),
        ('overweight', 'Избыточный вес'),
        ('obese_1', 'Ожирение I степени'),
        ('obese_2', 'Ожирение II степени'),
    ], verbose_name="Категория ИМТ")

    # Additional notes
    additional_notes = models.TextField(null=True, blank=True, verbose_name="Дополнительные заметки")

    class Meta:
        verbose_name = "Запись о здоровье"
        verbose_name_plural = "Записи о здоровье"

    def __str__(self):
        return f"Запись о здоровье пользователя {self.user.email} от {self.health_id}"
