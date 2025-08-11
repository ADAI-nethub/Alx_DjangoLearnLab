from django.db import models

<<<<<<< HEAD

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.author} ({self.publication_year})"
=======
# Create your models here.
>>>>>>> 7db3ed74b335d7e07e77c718d276cfad962fcedb
