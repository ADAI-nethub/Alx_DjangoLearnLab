from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    # Optional: show author name in the response
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'publication_year', 'owner']
        read_only_fields = ['owner']  # prevent manual assignment via API

    def validate_publication_year(self, value):
        """Custom validation for publication year"""
        if value < 0:
            raise serializers.ValidationError("Publication year cannot be negative.")
        return value

    def create(self, validated_data):
        """Ensure the owner is the logged-in user"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['owner'] = request.user
        return super().create(validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    # ✅ Nested relationship: include books written by the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
