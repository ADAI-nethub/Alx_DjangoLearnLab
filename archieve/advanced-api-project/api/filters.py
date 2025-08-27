# api/filters.py

import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    publication_year__gt = django_filters.NumberFilter(
        field_name='publication_year', lookup_expr='gt'
    )
    publication_year__lt = django_filters.NumberFilter(
        field_name='publication_year', lookup_expr='lt'
    )

    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author__name': ['exact', 'icontains'],
            'publication_year': ['exact'],
        }
