from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..serializers import (
    LoginSerializer, SignUpSerializer, ChangePasswordSerializer,
    EmailConfirmationSerializer, PasswordResetSerializer, UserSerializer
)
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token


class SignUpView(APIView):
    """
    Регистрация нового пользователя.

    Принимает данные пользователя, создает пользователя и токен авторизации.
    Возвращает созданного пользователя и токен.
    """
    serializer_class = SignUpSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="username",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Имя пользователя"
            ),
            OpenApiParameter(
                name="email",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Email пользователя"
            ),
            OpenApiParameter(
                name="password",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Пароль пользователя"
            ),
            OpenApiParameter(
                name="first_name",
                type=str,
                location=OpenApiParameter.QUERY,
                required=False,
                description="Имя пользователя"
            ),
        ],
        responses={201: UserSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    serializer_class = LoginSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="email",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Email пользователя"
            ),
            OpenApiParameter(
                name="password",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Пароль пользователя"
            )
        ],
        responses={200: UserSerializer}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email, password=password)

        if not user:
            return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({'error': 'Пользователь заблокирован'}, status=status.HTTP_403_FORBIDDEN)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
    Выход пользователя из системы.

    Удаляет токен доступа авторизованного пользователя.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Отключает токен доступа для пользователя при выходе из системы.
        """
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    """
    Изменение пароля пользователя.

    Принимает старый и новый пароль пользователя в формате JSON.
    Возвращает сообщение об успешном изменении пароля или сообщение об ошибке при неудачной попытке.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="old_password",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Старый пароль пользователя"
            ),
            OpenApiParameter(
                name="new_password",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Новый пароль пользователя"
            ),
        ],
        responses={200: "Password changed successfully"}
    )
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')

        if not user.check_password(old_password):
            raise ValidationError({'old_password': 'Неправильный текущий пароль'})

        user.set_password(new_password)
        user.save()
        return Response({'message': 'Пароль успешно изменен'}, status=status.HTTP_200_OK)


class EmailConfirmationView(APIView):
    """
    Подтверждение адреса электронной почты пользователя.

    Принимает адрес электронной почты пользователя в формате JSON.
    Отправляет электронное письмо с инструкциями по подтверждению адреса.
    """
    permission_classes = []

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="email",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Email пользователя"
            ),
        ],
        responses={200: "Email confirmation sent"}
    )
    def post(self, request):
        serializer = EmailConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        send_mail(
            'Подтверждение адреса электронной почты',
            f'Пройдите по ссылке для подтверждения: http://example.com/confirm/{uid}/{token}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

        return Response({'message': 'Письмо с подтверждением отправлено'}, status=status.HTTP_200_OK)


class PasswordResetView(APIView):
    """
    Сброс пароля пользователя.

    Принимает адрес электронной почты пользователя в формате JSON.
    Отправляет электронное письмо с инструкциями по сбросу пароля.
    """
    permission_classes = []

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="email",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Email пользователя"
            ),
        ],
        responses={200: "Password reset instructions sent"}
    )
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer

        # Здесь должна быть логика сброса пароля

        return Response({'message': 'Инструкции по сбросу пароля отправлены'}, status=status.HTTP_200_OK)

