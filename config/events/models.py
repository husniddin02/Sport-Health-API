from django.db import models
from users.models import UserProfile
from sports_facilities.models import SportsFacility

class Event(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Профиль пользователя")
    event_name = models.CharField("Название мероприятия", max_length=100)
    event_date = models.DateField("Дата мероприятия")
    location = models.CharField("Место проведения", max_length=100)
    description = models.TextField("Описание мероприятия", null=True, blank=True)
    organizer = models.CharField("Организатор мероприятия", max_length=100)
    facilities = models.ManyToManyField(SportsFacility, related_name="events", verbose_name="Спортобъекты", blank=True)

    def __str__(self):
        return f"{self.event_name} - {self.event_date}"

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
