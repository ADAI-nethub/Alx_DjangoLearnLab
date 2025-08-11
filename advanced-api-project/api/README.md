# Advanced API Project - Book API

## Endpoints

- `GET /books/` - List all books
- `GET /books/<id>/` - Retrieve a single book
- `POST /books/create/` - Create a book (auth required)
- `PUT /books/<id>/update/` - Update a book (auth + ownership required)
- `DELETE /books/<id>/delete/` - Delete a book (auth + ownership required)

## Permissions

- Read: Public
- Create/Update/Delete: Authenticated users only
- Only owners can modify or delete their books

## Notes

- Owner is auto-assigned on book creation
- All responses are wrapped with `status`, `message`, and `data`
