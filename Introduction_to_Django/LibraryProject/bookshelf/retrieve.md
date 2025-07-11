```python
from bookshelf.models import Book

# Retrieve all books
all_books = Book.objects.all()

# Print details of each book
for book in all_books:
    print(f"ID: {book.id}")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year: {book.publication_year}")
    print("-" * 20)

# Expected output:
# ID: 1
# Title: 1984
# Author: George Orwell
# Year: 1949
# --------------------
```