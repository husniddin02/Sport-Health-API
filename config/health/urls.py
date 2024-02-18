from django.urls import path
from .views import HealthListView, HealthDetailsView

urlpatterns = [
    # Получить список всех записей о здоровье или создать новую запись
    path('health/', HealthListView.as_view(), name='health-list'),

    # Получить информацию о конкретной записи о здоровье, обновить ее или удалить
    path('health/<int:pk>/', HealthDetailsView.as_view(), name='health-details'),
]
