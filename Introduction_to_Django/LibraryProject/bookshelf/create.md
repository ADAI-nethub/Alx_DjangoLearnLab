```python
from bookshelf.models import Book

# Create a new book
new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Output the created book
print(new_book)

# Expected output:
# <Book: 1984 by George Orwell (1949)>
```