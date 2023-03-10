from django.contrib import admin
from .models import Employee,Holiday,EmployeeLeave

# Register your models here.
admin.site.register(Employee)
admin.site.register(Holiday)
admin.site.register(EmployeeLeave)