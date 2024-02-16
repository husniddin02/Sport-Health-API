from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор мероприятия")
    event_name = models.CharField(max_length=255, verbose_name="Название мероприятия")
    event_date = models.DateField(verbose_name="Дата проведения мероприятия")
    location = models.CharField(max_length=255, verbose_name="Место проведения мероприятия")
    description = models.TextField(verbose_name="Описание мероприятия")
    organizer = models.CharField(max_length=100, verbose_name="Организатор мероприятия")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.event_name
