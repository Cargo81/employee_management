from rest_framework import serializers
from .models import (
    Department, Employee, EmployeeProfile
    ,Project
)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
#employee serializer
class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(
        source='department.department_name',
        read_only=True
    )
    class Meta:
        model=Employee
        fields='__all__'
        
#employee profile serializer
class EmployeeProfileSerializer(serializers.ModelSerializer):
    employee_name=serializers.CharField(
        source='employee.employee_name',
        read_only=True
    )
    class Meta:
        model = EmployeeProfile
        fields='__all__'
        
#Project serializer
class ProjectSerializer(serializers.ModelSerializer):
    employee_names = serializers.StringRelatedField(
        source='employees',
        many=True,
        read_only=True
    )
    class Meta:
        model = Project
        fields = '__all__'