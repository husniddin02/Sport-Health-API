from django.urls import path
from .views import LoginView, SignUpView, LogoutView, UserAPIView

urlpatterns = [
    path('api/v1/user/profile/', UserAPIView.as_view(), name="user-profile"),
    path('api/v1/user/signup/', SignUpView.as_view(), name='user-signup'),
    path('api/v1/user/login/', LoginView.as_view(), name='user-login'),
    path('api/v1/user/logout/', LogoutView.as_view(), name='user-logout'),
]
