from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    created = models.DateField(auto_now_add=True)
    to_watch = models.ManyToManyField(Movie,related_name='towatch')
    watched = models.ManyToManyField(Movie, related_name='watched')