# urls.py

from django.urls import path
from .views import SportsFacilityListView, SportsFacilityDetailsView

urlpatterns = [
    path('sport-facilities/', SportsFacilityListView.as_view(), name='sport-facility-list'),
    path('sport-facilities/<int:pk>/', SportsFacilityDetailsView.as_view(), name='sport-facility-detail'),
]
