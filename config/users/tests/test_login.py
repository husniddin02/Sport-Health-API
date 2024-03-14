# users/tests/test_login.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_login_user_success():
    client = APIClient()
    url = reverse('login')
    user_data = {
        'email': 'test@example.com',
        'password': 'testpassword'
    }
    client.post(url, user_data, format='json')
    response = client.post(url, user_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'token' in response.data

@pytest.mark.django_db
def test_login_user_invalid_credentials():
    client = APIClient()
    url = reverse('login')
    user_data = {
        'email': 'test@example.com',
        'password': 'wrongpassword'
    }
    response = client.post(url, user_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'non_field_errors' in response.data
