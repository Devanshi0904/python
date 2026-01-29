from rest_framework import serializers
from company.models import *


class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dept
        fields='__all__'

    def to_representation(self, instance):
        resp =  super().to_representation(instance)
        resp['company'] = Companyserializer(instance.company).data
        return resp


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'
        # depth = 1   

    def to_representation(self, instance):
        resp =  super().to_representation(instance)
        resp['dept'] = DeptSerializer(instance.dept).data
        return resp


        