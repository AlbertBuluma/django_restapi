from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeserializer
