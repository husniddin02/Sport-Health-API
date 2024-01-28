from django.db import models
from django.contrib.auth.models import User
# create new model

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    height = models.DecimalField("Рост", max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField("Вес", max_digits=5, decimal_places=2, null=True, blank=True)
    blood_pressure = models.CharField("Давление", max_length=20, null=True, blank=True)
    heart_rate = models.IntegerField("Пульс", null=True, blank=True)
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)

    GENDER_CHOICES = [
        ('Male', 'Мужской'), 
        ('Female', 'Женский'),
    ]
    gender = models.CharField("Пол", max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    address = models.TextField("Адрес", null=True, blank=True)
    profile_photo = models.ImageField("Фото профиля", upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

        