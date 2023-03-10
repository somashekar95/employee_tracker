from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    leave_available = models.PositiveIntegerField()

    def __str__(self):
     return self.user.username


class Holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EmployeeLeave(models.Model):
    date = models.DateField()
    reason = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.user.email} - {self.date}"

