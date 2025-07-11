```python
from bookshelf.models import Book

# Get the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()  # Don't forget to save!

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

# Expected output:
# Nineteen Eighty-Four
```