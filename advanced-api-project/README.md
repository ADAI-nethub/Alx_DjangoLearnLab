## Book API Endpoints

### List Books
- **URL**: `/api/books/`
- **Method**: `GET`
- **Permissions**: Public
- **Response**: List of all books

### Create Book
- **URL**: `/api/books/create/`
- **Method**: `POST`
- **Permissions**: Authenticated users only
- **Body**: { "title": "string", "author": "string", ... }
- **Response**: Created book data

### Update Book
- **URL**: `/api/books/<id>/update/`
- **Method**: `PUT` or `PATCH`
- **Permissions**: Only the book owner
- **Body**: Fields to update
- **Response**: Updated book data

### Delete Book
- **URL**: `/api/books/<id>/delete/`
- **Method**: `DELETE`
- **Permissions**: Only the book owner
- **Response**: 204 No Content