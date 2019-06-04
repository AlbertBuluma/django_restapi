# from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from . models import employees
from .views import EmployeeView

class AccountTests(APITestCase):
    def test_create_employee(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('employees')
        data = {'firstname': 'DabApps', 'lastname': 'MyDabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(employees.objects.count(), 1)
        self.assertEqual(employees.objects.get().name, 'DabApps')
# Create your tests here.
