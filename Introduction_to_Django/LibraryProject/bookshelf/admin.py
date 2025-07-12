from django.contrib import admin
from .models import Book  # ✅ Import the Book model

# ✅ Register the Book model with Django Admin
admin.site.register(Book)