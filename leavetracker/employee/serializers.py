from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee, EmployeeLeave


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'user', 'age', 'gender', 'department', 'company_name', 'leave_available')


class LeaveSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = EmployeeLeave
        fields = ('id', 'date', 'reason', 'employee')

    def create(self, validated_data):
        employee_leave = EmployeeLeave.objects.create(**validated_data)
        return employee_leave

