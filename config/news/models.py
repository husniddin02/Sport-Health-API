# news/models.py

from django.db import models
from sportCategories.models import SportCategory

class News(models.Model):
    news_id = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор новости")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    publication_date = models.DateField(verbose_name="Дата публикации")
    author = models.CharField(max_length=100, verbose_name="Автор")
    category = models.ForeignKey(SportCategory, on_delete=models.CASCADE, verbose_name="Категория")
    details_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на подробности")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
