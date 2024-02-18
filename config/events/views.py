from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventListView(generics.ListCreateAPIView):
    """
    Список мероприятий.

    Получение списка всех мероприятий или создание нового мероприятия.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Поиск мероприятий по названию',
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
                'event_name': openapi.Schema(type=openapi.TYPE_STRING, description='Название мероприятия'),
                'event_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Дата проведения мероприятия'),
                # Добавьте остальные свойства здесь...
            },
            required=['event_name', 'event_date']
        )
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class EventDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали мероприятия.

    Получение, обновление или удаление информации о конкретном мероприятии.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
