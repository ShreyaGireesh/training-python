from rest_framework import serializers
from .models import Author, Book

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email']

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'published_date', 'author']

class AuthorHyperLinked(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name', 'email']

class BookHyperLinked(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name = 'author-detail', queryset = Author.objects.all())

    class Meta:
        model = Book
        fields = ['url', 'title', 'published_date', 'author']