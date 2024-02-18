from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import SportsFacility
from .serializers import SportsFacilitySerializer

class SportsFacilityListView(generics.ListCreateAPIView):
    """
    Спортивные объекты (SportsFacilities).

    * Получить список всех спортивных объектов.
    * Создать новый спортивный объект.
    """
    queryset = SportsFacility.objects.all()
    serializer_class = SportsFacilitySerializer

    @swagger_auto_schema(operation_description="Получить список всех спортивных объектов")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Создать новый спортивный объект")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SportsFacilityDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали спортивного объекта.

    * Получить информацию о конкретном спортивном объекте.
    * Обновить информацию о спортивном объекте.
    * Удалить спортивный объект.
    """
    queryset = SportsFacility.objects.all()
    serializer_class = SportsFacilitySerializer

    @swagger_auto_schema(operation_description="Получить информацию о конкретном спортивном объекте")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Обновить информацию о спортивном объекте")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Удалить спортивный объект")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
