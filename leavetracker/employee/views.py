from django.shortcuts import render

from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from datetime import date

from .models import Employee, Holiday, EmployeeLeave, User
from .serializers import EmployeeSerializer, LeaveSerializer


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user_email = self.request.data.get('email')
        user = User.objects.filter(email=user_email).first()
        if not user:
            raise serializers.ValidationError('No user found with the provided email')
        serializer.save(user=user)

    def get_queryset(self):
        return Employee.objects.none()



class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeUpdateView(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDeleteView(generics.DestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Employee.objects.all()


class LeaveApplyView(generics.CreateAPIView):
    serializer_class = LeaveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return EmployeeLeave.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        employee = Employee.objects.filter(user=user).first()
        if not employee:
            raise serializers.ValidationError('No employee found for the current user')

        dates = self.request.data.get('dates')
        reasons = self.request.data.get('reasons')
        for i in range(len(dates)):
            holiday = Holiday.objects.filter(date=dates[i]).first()
            if holiday:
                serializer.save(date=dates[i], reason=reasons[i], employee=employee)
            else:
                if employee.leave_available > 0:
                    employee.leave_available -= 1
                    employee.save()
                    serializer.save(date=dates[i], reason=reasons[i], employee=employee)
                else:
                    raise serializers.ValidationError('No more leave available for the employee')



