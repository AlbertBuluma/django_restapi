from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, APIClient, URLPatternsTestCase
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
    
    client = APIClient()
    client.post('/<int:id>', {firstname:'Jerry'}, format='json')
    # Testing Employee creation
    def test_Employee_names(self): 
        employee = Employees.objects.create(firstname='Albert', lastname='Buluma')
        employee.save()
        self.assertTrue(isinstance(employee, Employees))
        self.assertEqual(employee.firstname,'Albert')
        self.assertEqual(employee.lastname, 'Buluma')
   
    # Testing the API root view
    def test_Employee_list(self):
        url = reverse('api-root')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.data), 1)

    def test_Employee_update(self):
        employee2 = Employees.objects.filter(id=1)
        employee2.firstname='Van Dijk'
        # self.assertTrue(isinstance(employee2, Employees))
        self.assertEqual(employee2.firstname,'Van Dijk')

    # def test_Employee_id(self):
    #     count = Employees.objects.count()
    #     url = reverse('api-root/<int:id>',kwargs={id:Employees.object.get(id=1)})
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, 200)
    


    # def test_update_post(self):
    #     post = Posts.objects.create(id=5, fname='Namayanja', sname='Masitula', sex='female', amount='9000000')

    #     response = self.client.post(
    #         reverse('update-entry',kwargs={'id':post.id}), 
    #         {'fname': 'Namayanja', 'sname': 'Masitula', 'sex':'female', 'amount':9000000})
    #     self.assertEqual(response.status_code, 302)
    #     post.refresh_from_db()
    #     self.assertEqual(post.fname, 'Namayanja')
