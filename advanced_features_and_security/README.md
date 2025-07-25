# LibraryProject\nThis is a Django web application for managing a library system.
# Permissions and Groups Setup

This application uses Django's permission and group system to control access.

## Custom Permissions

Defined in `Book` model (`bookshelf/models.py`):

- `can_view`: Can view books
- `can_create`: Can create books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

## Groups

Configured via Django Admin:

- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_create`, `can_edit`
- **Admins**: Assigned all permissions

## Views

Permissions are enforced using `@permission_required` decorators:

- `/books/`: Requires `can_view`
- `/books/create/`: Requires `can_create`
- `/books/edit/<id>/`: Requires `can_edit`
- `/books/delete/<id>/`: Requires `can_delete`

## Testing

Create users and assign them to the above groups. Attempt to access views to validate permissions enforcement.

## Admin

Permissions and groups can be managed from the Django admin dashboard at `/admin/`.


