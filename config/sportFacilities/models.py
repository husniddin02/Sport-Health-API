from django.db import models

class SportsFacility(models.Model):
    facility_id = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор спортивного объекта")
    facility_name = models.CharField(max_length=100, verbose_name="Название спортивного объекта")
    location = models.CharField(max_length=255, verbose_name="Расположение")
    capacity = models.IntegerField(verbose_name="Вместимость")
    equipment_available = models.BooleanField(default=False, verbose_name="Наличие оборудования")
    trainer_available = models.BooleanField(default=False, verbose_name="Наличие тренера")

    class Meta:
        verbose_name = "Спортивный объект"
        verbose_name_plural = "Спортивные объекты"

    def __str__(self):
        return self.facility_name


class FacilityDetails(models.Model):
    facility = models.OneToOneField(SportsFacility, on_delete=models.CASCADE, related_name='details', verbose_name="Спортивный объект")
    details_link = models.URLField(max_length=200, verbose_name="Ссылка на дополнительные данные")

    class Meta:
        verbose_name = "Подробности спортивного объекта"
        verbose_name_plural = "Подробности спортивных объектов"

    def __str__(self):
        return self.facility.facility_name + " - " + self.details_link
