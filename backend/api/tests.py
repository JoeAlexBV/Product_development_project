from django.test import TestCase
from .models import Risk


class GetAllRisksTest(TestCase):
    """ Test module for Risk model """

    def setUp(self):
        self.car = Risk.objects.create(risk_type='Car')
        self.boat = Risk.objects.create(risk_type='Boat')
        # Risk.objects.create(risk_type='Car')
        # Risk.objects.create(risk_type='Boat')

    def test_Risk_type(self):
        Risk_car = Risk.objects.get(risk_type='Car')
        Risk_boat = Risk.objects.get(risk_type='Boat')
        self.assertEqual(
            Risk_car.get_risk(), "Car belongs to Car Risk Type.")
        self.assertEqual(
            Risk_boat.get_risk(), "Boat belongs to Boat Risk Type.")