from django.test import TestCase
from users.models import User
from .models import Health

class HealthModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем пользователя для тестирования
        test_user = User.objects.create_user(email='test@example.com', password='testpass')
        test_user.save()

    def setUp(self):
        # Создаем объект Health для каждого теста
        self.health = Health.objects.create(
            user=User.objects.get(email='test@example.com'),
            height=180.5,
            weight=75.0,
            heart_rate=70,
            bmi=23.1,
            bmi_category='normal',
            additional_notes='Регулярные упражнения и здоровое питание'
        )

    def test_health_creation(self):
        """Тест на создание записи о здоровье."""
        self.assertIsInstance(self.health, Health)
        self.assertEqual(self.health.height, 180.5)
        self.assertEqual(self.health.weight, 75.0)
        self.assertEqual(self.health.heart_rate, 70)
        self.assertEqual(self.health.bmi, 23.1)
        self.assertEqual(self.health.bmi_category, 'normal')
        self.assertEqual(self.health.additional_notes, 'Регулярные упражнения и здоровое питание')

    def test_health_string_representation(self):
        """Тест на строковое представление записи о здоровье."""
        expected_str = f"Запись о здоровье пользователя test@example.com от {self.health.pk}"
        self.assertEqual(str(self.health), expected_str)

    def test_health_user_relationship(self):
        """Тест на связь между записью о здоровье и пользователем."""
        self.assertEqual(self.health.user.email, 'test@example.com')

    def test_health_defaults(self):
        """Тест на значения по умолчанию."""
        default_health = Health.objects.create(user=User.objects.get(email='test@example.com'))
        self.assertIsNone(default_health.height)
        self.assertIsNone(default_health.weight)
        self.assertIsNone(default_health.heart_rate)
        self.assertIsNone(default_health.bmi)
        self.assertIsNone(default_health.bmi_category)
        self.assertIsNone(default_health.additional_notes)
