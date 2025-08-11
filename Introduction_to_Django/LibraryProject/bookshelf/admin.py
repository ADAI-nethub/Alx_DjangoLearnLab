from django.contrib import admin
<<<<<<< HEAD
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')
=======

# Register your models here.
>>>>>>> 7db3ed74b335d7e07e77c718d276cfad962fcedb
