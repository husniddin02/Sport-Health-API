# health/urls.py
from django.urls import path
from .views import HealthListAPIView

urlpatterns = [
    path('health/', HealthListAPIView.as_view(), name='health-list'),
]
