"""
The AuthorSerializer includes a nested BookSerializer to represent the one-to-many
relationship between authors and books. When serializing an author, all their
related books will be included in the output.

The BookSerializer includes custom validation to ensure data integrity for the
publication_year field.
"""
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Changed from CharField to ForeignKey
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields here
    
    def __str__(self):
        return self.user.username

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    # Add other workshop fields
    
    def __str__(self):
        return self.title

class Story(models.Model):
    title = models.CharField(max_length=200)
    # Add other story fields
    
    def __str__(self):
        return self.title
    
    