from bookshelf.models import Book

# Retrieve a specific book by title
book = Book.objects.get(title="1984")

# Print the book's details
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.publication_year}")
