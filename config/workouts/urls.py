from django.urls import path
from .views import WorkoutListView, WorkoutDetailsView

urlpatterns = [
    path('workouts/', WorkoutListView.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', WorkoutDetailsView.as_view(), name='workout-detail'),
]
