from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'publication_date']
    list_filter = ['category', 'publication_date']
    search_fields = ['title', 'content', 'author']

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'category', 'publication_date')
        }),
        ('Подробности', {
            'fields': ('details_link',),
            'classes': ('collapse',),
        }),
    )
