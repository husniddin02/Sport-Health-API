from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User

class UserAuthenticationTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('user-signup')
        self.login_url = reverse('user-login')
        self.user_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password': 'password123',
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_signup(self):
        response = self.client.post(self.signup_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login(self):
        login_data = {
            'email': 'testuser@example.com',  # Поменяйте на правильный email
            'password': 'password123',        # Поменяйте на правильный пароль
        }
        
        # Add CSRF token to the headers
        response = self.client.post(self.login_url, login_data, format='json', HTTP_X_CSRFTOKEN='dummy')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
