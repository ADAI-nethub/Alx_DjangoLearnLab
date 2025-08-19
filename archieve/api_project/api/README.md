## API Filtering/Searching/Ordering

### Filtering
- Filter by exact title: `?title=Harry Potter`
- Filter by partial title: `?title__icontains=potter`
- Filter by author name: `?author__name=Rowling`
- Filter by publication year range:
  - `?publication_year__gt=2000` (after 2000)
  - `?publication_year__lt=2010` (before 2010)

### Searching
- Search across multiple fields: `?search=Harry`

### Ordering
- Order by field: `?ordering=title` (ascending)
- Reverse order: `?ordering=-publication_year` (descending)
- Default ordering is by title ascending