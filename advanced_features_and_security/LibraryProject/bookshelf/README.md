# Permissions and Groups Setup - LibraryProject

## Custom Permissions Added

In `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups Created (via Admin)
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: All permissions

## Views Protected
- `book_list`: requires can_view
- `book_create`: requires can_create
- `book_edit`: requires can_edit
- `book_delete`: requires can_delete

## How to Test
1. Create test users.
2. Assign to groups.
3. Log in and test access to `/books`, `/books/create`, etc.

