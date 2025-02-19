from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Magazine
from .serializers import AuthorSerializer, MagazineSerializer
# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer