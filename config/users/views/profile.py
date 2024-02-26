# users/views/auth.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import User
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
        Возвращает объект пользователя по его идентификатору (pk).
        """
        pk = self.kwargs.get('pk')
        return User.objects.get(pk=pk)

    def destroy(self, request, *args, **kwargs):
        """
        Деактивирует аккаунт пользователя.

        Устанавливает поле `is_active` в значение `False` и сохраняет пользователя.
        """
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'message': 'Аккаунт пользователя деактивирован'}, status=status.HTTP_204_NO_CONTENT)

    def soft_destroy(self, request, *args, **kwargs):
        """
        Мягкое удаление аккаунта пользователя.

        Просто деактивирует пользователя, сохраняя данные для истории.
        """
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'message': 'Аккаунт пользователя деактивирован (мягкое удаление)'}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        """
        Создает нового пользователя.

        Пользователь должен быть аутентифицирован как суперпользователь для этой операции.
        """
        if not request.user.is_superuser:
            return Response({'error': 'Недостаточно прав доступа.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Обновляет данные профиля пользователя.

        Пользователь должен иметь доступ к своему профилю или быть суперпользователем.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if not request.user.is_superuser and instance != request.user:
            return Response({'error': 'Недостаточно прав доступа.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
