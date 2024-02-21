# users/urls.py
from django.urls import path
from .views import LoginView, SignUpView, LogoutView, UserAPIView, ChangePasswordView, EmailConfirmationView, PasswordResetView

urlpatterns = [
    path('api/v1/user/profile/', UserAPIView.as_view(), name="user-profile"),
    path('api/v1/user/signup/', SignUpView.as_view(), name='user-signup'),
    path('api/v1/user/login/', LoginView.as_view(), name='user-login'),
    path('api/v1/user/logout/', LogoutView.as_view(), name='user-logout'),
    path('api/v1/user/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/v1/user/email-confirmation/', EmailConfirmationView.as_view(), name='email-confirmation'),
    path('api/v1/user/password-reset/', PasswordResetView.as_view(), name='password-reset'),
]
