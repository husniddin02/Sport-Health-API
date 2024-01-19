from django.contrib import admin
from .models import SportCategory

class SportCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')
    search_fields = ('category_name',)

admin.site.register(SportCategory, SportCategoryAdmin)
