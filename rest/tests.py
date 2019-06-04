from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import routers
from rest.models import Employees
from . import views
# Create your tests here.

router = routers.DefaultRouter()
router.register('Employees', views.EmployeeView)


class EmployeeTestCase(TestCase):

    urlpatterns = [
        path('', include(router.urls),'api-root')
]

    def test_Employee_names(self): 
        employee = Employees.objects.create(firstname='Albert', lastname='Albert')
        #employee.save()
        self.assertEqual(employee.firstname,'Albert')

    def test_Employee_list(self):
        url = reverse('api-root')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.data), 1)

    def test_Employee_id(self):
        url = reverse('api-root/')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)