from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book, Author
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.client.login(username='testuser', password='pass')
        self.author = Author.objects.create(name='George Orwell')
        self.book = Book.objects.create(
            title="1984",
            author=self.author,
            owner=self.user,
            publication_year=1949
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 👇 Use of response.data 
        self.assertTrue(len(response.data) > 0)

    def test_detail_book(self):
        url = reverse('book-detail', args=[self.book.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_create_book(self):
        url = reverse('book-create')
        data = {
            'title': 'Animal Farm',
            'author': self.author.id,
            'owner': self.user.id,
            'publication_year': 1945
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Animal Farm')  # 👈 Added usage

    def test_update_book(self):
        url = reverse('book-update', args=[self.book.pk])
        data = {
            'title': 'Nineteen Eighty-Four',
            'author': self.author.id,
            'owner': self.user.id,
            'publication_year': 1949
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Nineteen Eighty-Four')  # 👈 Added usage

    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
