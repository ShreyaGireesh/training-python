from django.urls import path
from .views import EmpList, EmpCreate, EmpDetail

urlpatterns = [
    path('employees/', EmpList.as_view(), name='employee-list'),  # Anyone can view the employee list
    path('employees/create/', EmpCreate.as_view(), name='employee-create'),  # Only authenticated users can create
    path('employees/<int:pk>/', EmpDetail.as_view(), name='employee-detail'),  # Only authenticated users can view, update, or delete
]
