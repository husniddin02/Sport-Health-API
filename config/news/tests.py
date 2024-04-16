from django.test import TestCase
from .models import News
from sportCategories.models import SportCategory

class NewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = SportCategory.objects.create(
            name='Test Category',
            description='This is a test category'
        )
        News.objects.create(
            title='Test News',
            content='This is a test news content.',
            publication_date='2024-04-16',
            author='Test Author',
            category=category,
            details_link='https://example.com/test-news'
        )

    def test_news_title(self):
        """Тестирование поля заголовка новости."""
        news = News.objects.get(news_id=1)
        self.assertEqual(news.title, 'Test News')

    def test_news_content(self):
        """Тестирование поля содержания новости."""
        news = News.objects.get(news_id=1)
        self.assertEqual(news.content, 'This is a test news content.')

    def test_news_publication_date(self):
        """Тестирование поля даты публикации новости."""
        news = News.objects.get(news_id=1)
        self.assertEqual(str(news.publication_date), '2024-04-16')

    def test_news_author(self):
        """Тестирование поля автора новости."""
        news = News.objects.get(news_id=1)
        self.assertEqual(news.author, 'Test Author')

    def test_news_category(self):
        """Тестирование поля категории новости."""
        news = News.objects.get(news_id=1)
        category = SportCategory.objects.get(name='Test Category')
        self.assertEqual(news.category, category)

    def test_news_details_link(self):
        """Тестирование поля ссылки на подробности новости."""
        news = News.objects.get(news_id=1)
        self.assertEqual(news.details_link, 'https://example.com/test-news')

    def test_news_string_representation(self):
        """Тестирование строкового представления новости."""
        news = News.objects.get(news_id=1)
        expected_str = f"{news.title}"
        self.assertEqual(str(news), expected_str)
