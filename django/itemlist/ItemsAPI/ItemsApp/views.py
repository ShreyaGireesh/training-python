from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializers import ItemSerializer
# Create your views here.

@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def item_detail(request, id):
    try:
        item = Items.objects.get(id = id)
    except:
        return Response({'message':'Not Found'}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ItemSerializer(item, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = ItemSerializer(item)
        item.delete()
        return Response({'message': "deleted successfully",'item': serializer.data}, status= status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        item = Items.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

