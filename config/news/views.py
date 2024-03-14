# news/views.py

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

class NewsListView(generics.ListCreateAPIView):
    """
    Новости (News).

    * Получить список всех новостей.
    * Создать новую новость.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Поиск новостей по заголовку',
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
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Заголовок новости'),
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='Содержание новости'),
                'publication_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Дата публикации новости'),
                'author': openapi.Schema(type=openapi.TYPE_STRING, description='Автор новости'),
                'category_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID категории новости'),
                'details_link': openapi.Schema(type=openapi.TYPE_STRING, description='Ссылка на подробности'),
            },
            required=['title', 'content', 'publication_date', 'author', 'category_id']
        )
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class NewsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали новости.

    * Получить информацию о конкретной новости.
    * Обновить информацию о новости.
    * Удалить новость.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

