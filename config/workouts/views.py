from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutListView(generics.ListCreateAPIView):
    """
    Тренировки (Workouts).

    * Получить список всех тренировок.
    * Создать новую тренировку.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @swagger_auto_schema(operation_description="Получить список всех тренировок")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Создать новую тренировку")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class WorkoutDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детали тренировки.

    * Получить информацию о конкретной тренировке.
    * Обновить информацию о тренировке.
    * Удалить тренировку.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @swagger_auto_schema(operation_description="Получить информацию о конкретной тренировке")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Обновить информацию о тренировке")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Удалить тренировку")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
