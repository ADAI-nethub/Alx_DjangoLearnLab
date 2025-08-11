# Advanced API Project
A Django REST API that manages books and authors, complete with authentication and ownership tracking.
## Table of Contents
- Installation
- Features
- API Endpoints
- Usage
- Running Tests
- Contributing
- License

git clone https://github.com/yourusername/advanced-api-project.git
cd advanced-api-project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver

Key things your project can do.

JWT-authenticated API for books and authors

Custom user-based permissions

Publication year validation

Full CRUD functionality

Unit tests with APITestCase


GET    /api/books/         - List books  
POST   /api/books/create/  - Create book  
GET    /api/books/{id}/    - View book details  
PUT    /api/books/{id}/    - Update book  
DELETE /api/books/{id}/    - Delete book  

GET    /api/authors/       - List authors  
...


# Example with curl or Postman:
POST /api/token/ with username/password
Use the access token in headers:
Authorization: Bearer <your_token>


python manage.py test api

Fork the repo, create a new branch, push your changes, and open a pull request.
MIT License
