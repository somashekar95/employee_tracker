from django.urls import path
from .views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    LeaveApplyView,
)

urlpatterns = [
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/list/', EmployeeListView.as_view(), name='employee-list'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('leave/apply/', LeaveApplyView.as_view(), name='leave-apply'),
]

