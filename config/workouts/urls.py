# workouts/urls.py
from django.urls import path
from .views import WorkoutListAPIView, WorkoutDetailAPIView

urlpatterns = [
    path('workouts/', WorkoutListAPIView.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', WorkoutDetailAPIView.as_view(), name='workout-detail'),
]
