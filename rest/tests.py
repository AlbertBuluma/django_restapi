from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import routers
from rest.models import Employees
from . import views
# Create your tests here.

router = routers.DefaultRouter()
router.register('Employees', views.EmployeeView)

urlpatterns = [
        path('', include(router.urls),'api-root')
]

class EmployeeTestCase(TestCase):

    # def createEmployee(self):
    #     employee = Employees.object.create(firstname = 'Albert', lastname = 'Buluma')
    #     return employee

    #Testing the Employees model
    # def test_Employees_creation(self):
    #     created = self.createEmployee()
        # self.assertTrue(isinstance(created, Employees))
    #     self.assertEqual(created.__str__(), 'Albert')
    #     self.assertEqual(created.lastname, 'Buluma')

    def test_Employee_names(self): 
        employee = Employees.objects.create(firstname='Albert', lastname='Buluma')
        employee.save()
        self.assertTrue(isinstance(employee, Employees))
        self.assertEqual(employee.firstname,'Albert')
        self.assertEqual(employee.lastname, 'Buluma')
    # #testing the home view

    # def test_view_home(self):
    #     created = self.createUser()
    #     url = reverse('list-all')
    #     resp=self.client.get(url)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(created.fname, 'Faisal')

    # def test_update_post(self):
    #     post = Posts.objects.create(id=5, fname='Namayanja', sname='Masitula', sex='female', amount='9000000')

    #     response = self.client.post(
    #         reverse('update-entry',kwargs={'id':post.id}), 
    #         {'fname': 'Namayanja', 'sname': 'Masitula', 'sex':'female', 'amount':9000000})
    #     self.assertEqual(response.status_code, 302)
    #     post.refresh_from_db()
    #     self.assertEqual(post.fname, 'Namayanja')




    # def test_Employee_names(self): 
    #     employee = Employees.objects.create(firstname='Albert', lastname='Albert')
    #     #employee.save()
    #     self.assertEqual(employee.firstname,'Albert')

    # def test_Employee_list(self):
    #     url = reverse('api-root')
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.data), 1)

    # def test_Employee_id(self):
    #     count = Employees.objects.count()
    #     url = reverse('api-root/<int:id>',kwargs={id:Employees.object.get(id)})
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, 200)