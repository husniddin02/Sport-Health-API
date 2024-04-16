import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import User

@pytest.mark.django_db
def test_create_user_view():
    client = APIClient()
    url = reverse('user-list')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'height': 180,
        'weight': 75,
        'gender': 'Male'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='testuser').exists()
