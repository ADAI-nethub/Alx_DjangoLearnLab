from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        
        # Create the author (no user field here)
        self.author = Author.objects.create(name='George Orwell')

        # Create some books owned by the user and written by the author
        self.book1 = Book.objects.create(
            title="1984",
            author=self.author,
            owner=self.user,
            publication_year=1949
        )
        self.book2 = Book.objects.create(
            title="Brave New World",
            author=self.author,
            owner=self.user,
            publication_year=1932
        )

        # Log in the test client
        self.client.login(username='testuser', password='pass')
