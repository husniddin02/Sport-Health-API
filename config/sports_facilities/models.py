from django.db import models

class SportsFacility(models.Model):
    facility_name = models.CharField("Название спортобъекта", max_length=255)
    location = models.CharField("Местоположение спортобъекта", max_length=255)
    capacity = models.PositiveIntegerField("Вместимость спортобъекта")
    equipment_available = models.BooleanField("Наличие оборудования на спортобъекте")
    trainer_available = models.BooleanField("Наличие тренера на спортобъекте")

    def __str__(self):
        return self.facility_name

    class Meta:
        verbose_name = "Спортобъект"
        verbose_name_plural = "Спортобъекты"
