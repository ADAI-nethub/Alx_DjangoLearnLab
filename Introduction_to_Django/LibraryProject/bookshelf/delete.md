```python
from bookshelf.models import Book

# Get and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
remaining_books = Book.objects.all()
print(f"Books remaining: {remaining_books.count()}")

# Expected output:
# Books remaining: 0
```