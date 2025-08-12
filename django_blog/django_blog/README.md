# Django Blog – CRUD Features

## Features
- **List Posts** – `/` shows all blog posts.
- **View Post** – `/post/<id>/`
- **Create Post** – `/post/new/` (authenticated users only)
- **Edit Post** – `/post/<id>/edit/` (author only)
- **Delete Post** – `/post/<id>/delete/` (author only)

## Permissions
- Anonymous users: can view list & detail.
- Authenticated users: can create posts.
- Authors: can edit & delete their own posts.

## How to Run
```bash
python manage.py runserver


---

If you want, I can now **add this CRUD setup directly into your `django_blog` repo structure** so you can just drop it in.  
Do you want me to prepare that exact folder structure?
