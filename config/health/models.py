from django.db import models
from users.models import UserProfile

class Health(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name="Профиль пользователя")

    height = models.DecimalField("Рост", max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField("Вес", max_digits=5, decimal_places=2, null=True, blank=True)
    heart_rate = models.IntegerField("Пульс", null=True, blank=True)
    bmi = models.DecimalField("ИМТ", max_digits=5, decimal_places=2, null=True, blank=True)
    bmi_category = models.CharField("Категория ИМТ", max_length=20, null=True, blank=True)
    additional_notes = models.TextField("Дополнительные заметки о здоровье", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Расчет ИМТ
        if self.height and self.weight:
            self.bmi = self.weight / (self.height / 100) ** 2

            # Определение категории ИМТ
            if self.bmi < 18.5:
                self.bmi_category = "Недостаточный вес"
            elif 18.5 <= self.bmi < 25:
                self.bmi_category = "Нормальный вес"
            elif 25 <= self.bmi < 30:
                self.bmi_category = "Избыточный вес"
            else:
                self.bmi_category = "Ожирение"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Здоровье {self.user_profile.user.username}"

    class Meta:
        verbose_name = "Здоровье пользователя"
        verbose_name_plural = "Здоровье пользователей"
