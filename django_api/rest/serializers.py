from rest_framework import serializers
from . models import employees

# class employeeSerializer(serializers.ModelSerializer):
class employeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = employees
        fields = ('url','firstname','lastname')