# news/serializers.py
from rest_framework import serializers
from .models import News
from sportCategories.serializers import SportCategorySerializer

class NewsSerializer(serializers.ModelSerializer):
    category = SportCategorySerializer()

    class Meta:
        model = News
        fields = ['news_id', 'title', 'content', 'publication_date', 'author', 'category']
