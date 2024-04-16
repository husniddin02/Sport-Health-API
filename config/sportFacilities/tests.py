from django.test import TestCase
from .models import SportsFacility, FacilityDetails

class SportsFacilityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SportsFacility.objects.create(
            facility_name='Test Facility',
            location='Test Location',
            capacity=100,
            equipment_available=True,
            trainer_available=False
        )

    def test_facility_name(self):
        """Тестирование поля название спортивного объекта."""
        facility = SportsFacility.objects.get(facility_id=1)
        self.assertEqual(facility.facility_name, 'Test Facility')

    def test_facility_location(self):
        """Тестирование поля расположение спортивного объекта."""
        facility = SportsFacility.objects.get(facility_id=1)
        self.assertEqual(facility.location, 'Test Location')

    def test_facility_capacity(self):
        """Тестирование поля вместимость спортивного объекта."""
        facility = SportsFacility.objects.get(facility_id=1)
        self.assertEqual(facility.capacity, 100)

    def test_facility_equipment_available(self):
        """Тестирование поля наличие оборудования спортивного объекта."""
        facility = SportsFacility.objects.get(facility_id=1)
        self.assertTrue(facility.equipment_available)

    def test_facility_trainer_available(self):
        """Тестирование поля наличие тренера спортивного объекта."""
        facility = SportsFacility.objects.get(facility_id=1)
        self.assertFalse(facility.trainer_available)


class FacilityDetailsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        facility = SportsFacility.objects.create(
            facility_name='Test Facility',
            location='Test Location',
            capacity=100,
            equipment_available=True,
            trainer_available=False
        )
        FacilityDetails.objects.create(
            facility=facility,
            details_link='https://example.com/details'
        )

    def test_details_link(self):
        """Тестирование поля ссылка на дополнительные данные."""
        details = FacilityDetails.objects.get(id=1)
        self.assertEqual(details.details_link, 'https://example.com/details')

    def test_details_string_representation(self):
        """Тестирование строкового представления подробности спортивного объекта."""
        details = FacilityDetails.objects.get(id=1)
        expected_str = f"{details.facility.facility_name} - {details.details_link}"
        self.assertEqual(str(details), expected_str)
