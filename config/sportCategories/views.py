from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import SportCategory
from .serializers import SportCategorySerializer

class SportCategoryListView(generics.ListCreateAPIView):
    """
    Категории спорта (SportCategories).

    * Получить список всех категорий спорта.
    * Создать новую категорию спорта.
    """
    queryset = SportCategory.objects.all()
    serializer_class = SportCategorySerializer

    @swagger_auto_schema(operation_description="Получить список всех категорий спорта")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Создать новую категорию спорта")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SportCategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали категории спорта.

    * Получить информацию о конкретной категории спорта.
    * Обновить информацию о категории спорта.
    * Удалить категорию спорта.
    """
    queryset = SportCategory.objects.all()
    serializer_class = SportCategorySerializer

    @swagger_auto_schema(operation_description="Получить информацию о конкретной категории спорта")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Обновить информацию о категории спорта")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Удалить категорию спорта")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
