# config/urls.py
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('', include('workouts.urls')),
    path('', include('news.urls')),
    path('', include('sportCategories.urls')),
    path('', include('sportFacilities.urls')),
    path('', include('users.urls')),
    path('', include('events.urls')),
    path('', include('health.urls')),
]

urlpatterns += doc_urls