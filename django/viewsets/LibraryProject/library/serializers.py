from rest_framework import serializers
from .models import Author, Magazine

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name', 'email']

class MagazineSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', queryset=Author.objects.all())

    class Meta:
        model = Magazine
        fields = ['url', 'title', 'publication_date', 'author']
