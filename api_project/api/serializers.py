
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn']


from rest_framework import serializers
from .models import Workshop, Story, UserProfile

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'  # Serializes all fields from the Workshop model

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'  # Serializes all fields from the Story model

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'role', 'points']  # Only these fields are serialized


