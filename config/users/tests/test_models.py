from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем пользователя для тестирования
        cls.user = get_user_model().objects.create_user(
            email='test@example.com',
            username='testuser',
            first_name='Test',
            last_name='User',
            avatar=None,
            height=180,
            weight=75,
            date_of_birth=date(1990, 1, 1),
            gender='Male',
            is_staff=False,
            is_superuser=False,
        )

    def test_user_str_representation(self):
        """Тестирование строкового представления пользователя."""
        user = get_user_model().objects.get(pk=self.user.pk)
        expected_str = f"({user.id}) {user.username}"
        self.assertEqual(str(user), expected_str)

    def test_user_full_name(self):
        """Тестирование метода get_full_name() для пользователя."""
        user = get_user_model().objects.get(pk=self.user.pk)
        expected_full_name = f"{user.first_name} {user.last_name}"
        self.assertEqual(user.get_full_name(), expected_full_name)

    def test_user_short_name(self):
        """Тестирование метода get_short_name() для пользователя."""
        user = get_user_model().objects.get(pk=self.user.pk)
        self.assertEqual(user.get_short_name(), user.username)

    def test_user_age_calculation(self):
        """Тестирование вычисления возраста пользователя."""
        user = get_user_model().objects.get(pk=self.user.pk)
        today = date.today()
        expected_age = today.year - user.date_of_birth.year - ((today.month, today.day) < (user.date_of_birth.month, user.date_of_birth.day))
        self.assertEqual(user.age, expected_age)

    def test_user_email_label(self):
        """Тестирование метки поля электронной почты пользователя."""
        user = get_user_model().objects.get(pk=self.user.pk)
        email_field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(email_field_label, 'Эл.почта')

    def test_user_first_name_max_length(self):
        """Тестирование максимальной длины поля имени пользователя."""
        user = get_user_model().objects.get(pk=self.user.pk)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 65)



