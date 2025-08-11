from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book

admin.site.register(Book)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'is_staff', 'date_of_birth')
    search_fields = ('username', 'email')
admin.site.register(CustomUser, CustomUserAdmin)
