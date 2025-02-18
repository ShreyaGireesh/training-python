
from rest_framework import serializers
from .models import Manager, Developer, ActiveEmployee, InactiveEmployee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager  
        fields = ['name', 'email', 'dob', 'employee_id', 'is_active']

class ManagerSerializer(EmployeeSerializer):
    class Meta:
        model = Manager
        fields = EmployeeSerializer.Meta.fields + ['department', 'salary']


class DeveloperSerializer(EmployeeSerializer):
    class Meta:
        model = Developer
        fields = EmployeeSerializer.Meta.fields + ['programming_languages', 'salary']


class ActiveEmployeeSerializer(EmployeeSerializer):
    class Meta:
        model = ActiveEmployee
        fields = EmployeeSerializer.Meta.fields


class InactiveEmployeeSerializer(EmployeeSerializer):
    class Meta:
        model = InactiveEmployee
        fields = EmployeeSerializer.Meta.fields
