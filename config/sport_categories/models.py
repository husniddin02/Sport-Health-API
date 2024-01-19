from django.db import models

class SportCategory(models.Model):
    category_name = models.CharField("Название категории спорта", max_length=50)
    description = models.TextField("Описание категории спорта")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория спорта"
        verbose_name_plural = "Категории спорта"
