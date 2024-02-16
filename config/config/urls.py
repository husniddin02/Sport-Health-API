# config/urls.py
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('workouts.urls')),
    path('api/', include('news.urls')),
    path('api/', include('sportCategories.urls')),
    path('api/', include('sportFacilities.urls')),
    path('api/', include('users.urls')),
    path('api/', include('events.urls')),
    path('api/', include('health.urls')),
]

urlpatterns += doc_urls