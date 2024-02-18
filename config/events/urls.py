from django.urls import path
from .views import EventListView, EventDetailsView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailsView.as_view(), name='event-detail'),
]
