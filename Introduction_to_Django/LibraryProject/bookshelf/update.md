```python
from bookshelf.models import Book

# Get the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the change
print(book.title)

# Expected output:
# Nineteen Eighty-Four
```