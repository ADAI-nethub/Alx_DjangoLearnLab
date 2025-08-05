"""
The AuthorSerializer includes a nested BookSerializer to represent the one-to-many
relationship between authors and books. When serializing an author, all their
related books will be included in the output.

The BookSerializer includes custom validation to ensure data integrity for the
publication_year field and handles owner assignment automatically.
"""
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model with custom validation and owner handling"""
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'owner']
        extra_kwargs = {
            'owner': {'read_only': True},  # Owner is set automatically in views
            'author': {'required': True}   # Author must be provided
        }

    def validate_publication_year(self, value):
        """
        Validate that publication year is:
        - Not in the future
        - Reasonably recent (after 1800)
        """
        current_year = datetime.now().year
        if value < 1800:
            raise serializers.ValidationError("Publication year too far in the past")
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model with nested books relationship"""
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'books']
        extra_kwargs = {
            'bio': {'required': False}  # Bio is optional
        }