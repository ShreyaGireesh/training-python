# urls.py
from django.urls import path
from .views import ManagerListCreate, ManagerRetrieveUpdateDestroy, DeveloperListCreate, DeveloperRetrieveUpdateDestroy, ActiveEmployeeList, InactiveEmployeeList

urlpatterns = [
    path('managers/', ManagerListCreate.as_view(), name='manager-list-create'),
    path('managers/<int:pk>/', ManagerRetrieveUpdateDestroy.as_view(), name='manager-retrieve-update-destroy'),

    path('developers/', DeveloperListCreate.as_view(), name='developer-list-create'),
    path('developers/<int:pk>/', DeveloperRetrieveUpdateDestroy.as_view(), name='developer-retrieve-update-destroy'),

    path('active-employees/', ActiveEmployeeList.as_view(), name='active-employees-list'),
    path('inactive-employees/', InactiveEmployeeList.as_view(), name='inactive-employees-list'),
]
