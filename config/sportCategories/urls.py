from django.urls import path
from .views import SportCategoryListView, SportCategoryDetailsView

urlpatterns = [
    path('categories/', SportCategoryListView.as_view(), name='sportcategory-list'),
    path('categories/<int:pk>/', SportCategoryDetailsView.as_view(), name='sportcategory-detail'),
]
