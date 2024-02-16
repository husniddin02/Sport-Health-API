# sportCategories/urls.py
from django.urls import path
from .views import SportCategoryListAPIView

urlpatterns = [
    path('categories/', SportCategoryListAPIView.as_view(), name='category-list'),
]
