from django.db import models
from sport_categories.models import SportCategory

class News(models.Model):
    title = models.CharField("Заголовок новости", max_length=255)
    content = models.TextField("Содержание новости")
    publication_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.CharField("Автор новости", max_length=100)
    category = models.ForeignKey(SportCategory, on_delete=models.CASCADE, verbose_name="Категория спорта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
