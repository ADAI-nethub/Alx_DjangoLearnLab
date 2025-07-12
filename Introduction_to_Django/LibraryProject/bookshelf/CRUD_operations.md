# CRUD Operations for Book Model

## Create
```python
from bookshelf.models import Book
new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Output: <Book: 1984>
```

## Retrieve
```python
from bookshelf.models import Book
all_books = Book.objects.all()
for book in all_books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
# Output: Title: 1984, Author: George Orwell, Year: 1949
```

## Update
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four
```

## Delete
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# Output: <QuerySet []>
```