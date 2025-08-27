from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    # Social connections - who follows whom
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False,  # Following isn't automatic both ways
        related_name='following',  # Reverse relationship name
        blank=True
    )
    
    def __str__(self):
        return self.username
    
    def follow(self, user):
        """Follow another user"""
        if user != self and user not in self.following.all():
            self.following.add(user)
            return True
        return False
    
    def unfollow(self, user):
        """Unfollow a user"""
        if user in self.following.all():
            self.following.remove(user)
            return True
        return False
    
    @property
    def followers_count(self):
        return self.followers.count()
    
    @property
    def following_count(self):
        return self.following.count()