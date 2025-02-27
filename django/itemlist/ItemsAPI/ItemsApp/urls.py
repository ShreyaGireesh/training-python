from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list, name='item_list'),
    path('items/<int:id>', views.item_detail, name='item_details')
]