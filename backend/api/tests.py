import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Risk
from .serializers import RiskSerializer

client = Client()


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

    def test_get_all_risks(self):
        # get API response
        response = client.get(reverse('get_post_risks'))
        # get data from db
        risks = Risk.objects.all()
        serializer = RiskSerializer(risks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRiskTest(TestCase):

    def setUp(self):
        self.car = Risk.objects.create(risk_type='Car')
        self.boat = Risk.objects.create(risk_type='Boat')

    def test_get_valid_single_risk(self):
        response = client.get(
            reverse('get_delete_update_risk', kwargs={'pk': self.car.pk}))
        risk = Risk.objects.get(pk=self.car.pk)
        serializer = RiskSerializer(risk)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewRiskTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'risk_type': 'Home',
            'fieldz': [
                {
                    "name": "firstname",
                    "field_type": "Text"
                },
                {
                    "name": "lastname",
                    "field_type": "Text"
                },
                {
                    "name": "Address",
                    "field_type": "Text"
                }
            ]
        }

    def test_create_valid_risk(self):
        response = client.post(
            reverse('get_post_risks'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)