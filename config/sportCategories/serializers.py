from rest_framework import serializers
from .models import SportCategory

class SportCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCategory
        fields = ['category_id', 'category_name', 'description']

    def create(self, validated_data):
        return SportCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
