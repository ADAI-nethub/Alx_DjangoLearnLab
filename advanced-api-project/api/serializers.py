from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name="Author Name")
        self.client.force_authenticate(user=self.user)  # Authenticate the client

    def test_create_book(self):
        url = reverse('book-list')  # adjust this name based on your router config
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2005,
        }
        response = self.client.post(url, data, format='json')  # Make sure to use format='json'

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().owner, self.user)
