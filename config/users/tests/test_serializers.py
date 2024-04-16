import pytest
from users.models import User
from users.serializers import UserSerializer

@pytest.mark.django_db
def test_user_serializer_create():
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'height': 180,
        'weight': 75,
        'gender': 'Male'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.height == 180
    assert user.weight == 75
    assert user.gender == 'Male'
