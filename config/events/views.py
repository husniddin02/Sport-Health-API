from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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
        operation_description="Получить список всех мероприятий",
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
        search = request.query_params.get('search', None)
        if search is not None:
            self.queryset = self.queryset.filter(event_name__icontains=search)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать новое мероприятие",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'event_name': openapi.Schema(type=openapi.TYPE_STRING, description='Название мероприятия'),
                'event_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Дата проведения мероприятия'),
                'location': openapi.Schema(type=openapi.TYPE_STRING, description='Место проведения мероприятия'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Описание мероприятия'),
                'organizer': openapi.Schema(type=openapi.TYPE_STRING, description='Организатор мероприятия'),
            },
            required=['event_name', 'event_date', 'location', 'description', 'organizer']
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
