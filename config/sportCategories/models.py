from django.db import models

class SportCategory(models.Model):
    category_id = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор категории спорта")
    category_name = models.CharField(max_length=100, verbose_name="Название категории спорта")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория спорта"
        verbose_name_plural = "Категории спорта"

    def __str__(self):
        return self.category_name
