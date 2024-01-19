from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author', 'category')
    search_fields = ('title', 'author')
    list_filter = ('category',)

admin.site.register(News, NewsAdmin)
