```python
from bookshelf.models import Book

# Get and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
print(Book.objects.all())

# Expected output:
# <QuerySet []>
```