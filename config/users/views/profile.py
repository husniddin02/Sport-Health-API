# users/views/profile.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status

from ..serializers import UserSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления данных пользователя.

    Предоставляет методы GET, DELETE и PATCH для работы с данными авторизованного пользователя.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "delete", "patch"]

    def get_object(self):
        """
        Возвращает объект пользователя, связанный с текущим запросом.
        """
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        """
        Деактивирует аккаунт пользователя.

        Устанавливает поле `is_active` в значение `False` и сохраняет пользователя.
        """
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)