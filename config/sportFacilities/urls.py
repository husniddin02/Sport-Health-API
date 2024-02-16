# sportFacilities/urls.py
from django.urls import path
from .views import SportsFacilityListAPIView

urlpatterns = [
    path('facilities/', SportsFacilityListAPIView.as_view(), name='facility-list'),
]
