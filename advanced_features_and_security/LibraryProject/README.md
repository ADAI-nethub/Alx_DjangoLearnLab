# LibraryProject

# LibraryProject

This Django app demonstrates permission and group management.

## Permissions Added
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: All permissions

## Setup
Permissions are enforced using `@permission_required` in views.

Test different users by assigning them to groups in the Django admin panel.
