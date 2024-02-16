# sportCategories/serializers.py
from rest_framework import serializers
from .models import SportCategory

class SportCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCategory
        fields = ['category_id', 'category_name', 'description']
