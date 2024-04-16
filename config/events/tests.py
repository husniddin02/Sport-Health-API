from django.test import TestCase
from .models import Event

class EventModelTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            event_name='Test Event',
            event_date='2024-04-20',
            location='Test Location',
            description='This is a test event',
            organizer='Test Organizer'
        )

    def test_event_creation(self):
        """Тестирование создания события."""
        self.assertEqual(self.event.event_name, 'Test Event')
        self.assertEqual(self.event.event_date, '2024-04-20')
        self.assertEqual(self.event.location, 'Test Location')
        self.assertEqual(self.event.description, 'This is a test event')
        self.assertEqual(self.event.organizer, 'Test Organizer')

    def test_event_str_representation(self):
        """Тестирование строкового представления события."""
        self.assertEqual(str(self.event), 'Test Event')

    def test_event_verbose_name_plural(self):
        """Тестирование множественного числа для verbose_name_plural."""
        self.assertEqual(str(Event._meta.verbose_name_plural), 'Мероприятия')
