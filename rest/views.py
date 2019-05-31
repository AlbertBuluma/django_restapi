from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from . models import employees
from .serializers import employeeSerializer

class EmployeeView(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeeSerializer 