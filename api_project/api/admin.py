# api/admin.py
from django.contrib import admin
from .models import Author, Book, UserProfile, Workshop, Story

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'points')
    list_filter = ('role',)
    search_fields = ('user__username', 'bio')

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'location_name', 'date', 'host')
    list_filter = ('date', 'host')
    search_fields = ('title', 'description', 'location_name')
    date_hierarchy = 'date'

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'workshop', 'author', 'submitted_at')
    list_filter = ('workshop', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('workshop', 'author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'bio')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author__name')
    raw_id_fields = ('author',)