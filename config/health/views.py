from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import Health
from .serializers import HealthSerializer

class HealthListView(generics.ListCreateAPIView):
    """
    Записи о здоровье (Health).

    * Получить список всех записей о здоровье.
    * Создать новую запись о здоровье.
    """

    queryset = Health.objects.all()
    serializer_class = HealthSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Поиск записей о здоровье по названию',
                required=False,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'height': openapi.Schema(type=openapi.TYPE_NUMBER, description='Рост (см)'),
                'weight': openapi.Schema(type=openapi.TYPE_NUMBER, description='Вес (кг)'),
                'heart_rate': openapi.Schema(type=openapi.TYPE_INTEGER, description='Частота сердечных сокращений (уд./мин.)'),
                'bmi': openapi.Schema(type=openapi.TYPE_NUMBER, description='Индекс массы тела (ИМТ)'),
                'bmi_category': openapi.Schema(type=openapi.TYPE_STRING, description='Категория ИМТ'),
                'additional_notes': openapi.Schema(type=openapi.TYPE_STRING, description='Дополнительные заметки'),
            },
            required=['height', 'weight']
        )
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class HealthDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали записи о здоровье.

    * Получить информацию о конкретной записи о здоровье.
    * Обновить информацию о записи о здоровье.
    * Удалить запись о здоровье.
    """
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
