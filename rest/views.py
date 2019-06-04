from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from . models import Employees
from .serializers import employeeSerializer

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializer 