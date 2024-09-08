from rest_framework import Serializers
from .models import Author, book

class AuthorSerializer(serializers.ModelSerializer): #Serializer for the Author model with a field name.
    class Meta:
        model = Author
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer): #Serializer for Book with the fields title, publication_year and author
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

        def validate_publication_year(self, value):
            import datetime
            if value > datetime.datetime.now().year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value
