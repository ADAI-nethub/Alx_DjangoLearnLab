"""
The AuthorSerializer includes a nested BookSerializer to represent the one-to-many
relationship between authors and books. When serializing an author, all their
related books will be included in the output.

The BookSerializer includes custom validation to ensure data integrity for the
publication_year field.
"""

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model with custom validation"""
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Validate that publication year is not in the future"""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model with nested BookSerializer"""
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']