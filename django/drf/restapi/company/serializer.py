from rest_framework import serializers
from company.models import *

class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dept
        fields='__all__'


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'
        depth = 1

        