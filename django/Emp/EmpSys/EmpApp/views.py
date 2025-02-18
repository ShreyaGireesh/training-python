from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Manager, Developer, ActiveEmployee, InactiveEmployee
from .serializers import ManagerSerializer, DeveloperSerializer, ActiveEmployeeSerializer, InactiveEmployeeSerializer
# Create your views here.

class ManagerListCreate(APIView):
    """ 
    Handles both list all managers and create a new manager requests for managers.
    """
    def get(self, request, *args, **kwargs):
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagerRetrieveUpdateDestroy(APIView):
    """
    Handles retrieve, update, and delete requests for a specific manager based on pk. 
    """
    def get(self, request, pk, *args, **kwargs):
        try:
            manager = Manager.objects.get(pk=pk)
        except Manager.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ManagerSerializer(manager)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            manager = Manager.objects.get(pk=pk)
        except Manager.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ManagerSerializer(manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            manager = Manager.objects.get(pk=pk)
        except Manager.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Developer CRUD View
class DeveloperListCreate(APIView):
    """ 
    Handles list all developers and create a new developer requests for developers.
    """
    def get(self, request, *args, **kwargs):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeveloperRetrieveUpdateDestroy(APIView):
    """ 
    Handles retrieve, update, and delete requests for a specific developer based on pk.
    """
    def get(self, request, pk, *args, **kwargs):
        try:
            developer = Developer.objects.get(pk=pk)
        except Developer.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            developer = Developer.objects.get(pk=pk)
        except Developer.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DeveloperSerializer(developer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            developer = Developer.objects.get(pk=pk)
        except Developer.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Active Employees View
class ActiveEmployeeList(APIView):
    """ 
    Custom view to list only active employees using the ActiveEmployee proxy model.
    """
    def get(self, request, *args, **kwargs):
        active_employees = ActiveEmployee.objects.filter(is_active=True)
        serializer = ActiveEmployeeSerializer(active_employees, many=True)
        return Response(serializer.data)

# Inactive Employees View
class InactiveEmployeeList(APIView):
    """ 
    Custom view to list only inactive employees using the InactiveEmployee proxy model.
    """
    def get(self, request, *args, **kwargs):
        inactive_employees = InactiveEmployee.objects.filter(is_active=False)
        serializer = InactiveEmployeeSerializer(inactive_employees, many=True)
        return Response(serializer.data)
