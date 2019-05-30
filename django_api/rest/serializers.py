from rest_framework import serializers
from rest_framework import serializers
from . models import employees

class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = '__all__'  #display all model fields