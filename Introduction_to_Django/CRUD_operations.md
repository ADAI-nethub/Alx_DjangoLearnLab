# CRUD Operations Documentation

## 1. Create Operation
```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```
**Output:**
```
Created: 1984 by George Orwell
```

## 2. Retrieve Operation
```python
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.publication_year}")
```
**Output:**
```
Title: 1984
Author: George Orwell
Year: 1949
```

## 3. Update Operation
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```
**Verification Output:**
```
After Update:
New Title: Nineteen Eighty-Four
```

## 4. Delete Operation
```python
Book.objects.get(title="Nineteen Eighty-Four").delete()
```
**Verification Output:**
```
After Delete:
Books in DB: 0
```