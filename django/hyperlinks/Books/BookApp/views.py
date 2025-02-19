from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializers, BookSerializers, AuthorHyperLinked, BookHyperLinked

# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

# hyperlinked
class AuthorHyperlinkedListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorHyperLinked

class AuthorHyperlinkedDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorHyperLinked

class BookHyperlinkedListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookHyperLinked

class BookHyperlinkedDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookHyperLinked
