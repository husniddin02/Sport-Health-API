from django.test import TestCase
from .models import SportCategory

class SportCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SportCategory.objects.create(
            category_name='Test Category',
            description='This is a test category'
        )

    def test_category_name(self):
        """Тестирование поля название категории спорта."""
        category = SportCategory.objects.get(category_id=1)
        self.assertEqual(category.category_name, 'Test Category')

    def test_category_description(self):
        """Тестирование поля описание категории спорта."""
        category = SportCategory.objects.get(category_id=1)
        self.assertEqual(category.description, 'This is a test category')

    def test_category_string_representation(self):
        """Тестирование строкового представления категории спорта."""
        category = SportCategory.objects.get(category_id=1)
        expected_str = f"{category.category_name}"
        self.assertEqual(str(category), expected_str)
