from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# api/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('tourist', 'Tourist'),
        ('artist', 'Artist'),
        ('guide', 'Local Guide'),
        ('admin', 'Administrator'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tourist')
    points = models.BigIntegerField(default=0)  # Optional enhancement

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Workshop(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateField()
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="hosted_workshops")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} @ {self.location_name} on {self.date}"

class Story(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='stories')
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    media_url = models.URLField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Story: {self.title} by {self.author}"


from django.db import models
from django.contrib.auth.models import User

class Workshop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    bio = models.TextField(blank=True)