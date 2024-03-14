# news/serializers.py

from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['news_id', 'title', 'content', 'publication_date', 'author', 'category', 'details_link']

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.details_link = validated_data.get('details_link', instance.details_link)
        instance.save()
        return instance
