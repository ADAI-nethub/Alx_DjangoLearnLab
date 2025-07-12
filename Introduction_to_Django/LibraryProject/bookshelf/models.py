from django.contrib import admin
from .models import Book  # ✅ Import the Book model

# ✅ Register the Book model with Django Admin
admin.site.register(Book)

from django.db import models

class Book(models.Model):
    """
    A model representing a book in the bookshelf app.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
