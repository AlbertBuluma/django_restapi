from rest_framework import serializers
from . models import Employees

# class employeeSerializer(serializers.ModelSerializer):
class employeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employees
        fields = ('url','firstname','lastname')