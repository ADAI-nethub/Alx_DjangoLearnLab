# models.py
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):  # ✅ This class must exist!
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

