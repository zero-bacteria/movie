from django.db import models

class Genre(models.Model):
    genre_ids = models.CharField(max_length=50)

class Movie(models.Model):
    adult = models.BooleanField(default=False, blank=True)
    backdrop_path = models.CharField(max_length=100, blank=True)
    genre_ids = models.ManyToManyField(Genre, blank=True)
    movie_id = models.IntegerField(blank=True)
    original_language = models.CharField(max_length=100, blank=True)
    original_title = models.CharField(max_length=100, blank=True)
    overview = models.TextField(blank=True)
    popularity = models.FloatField(blank=True)
    poster_path = models.CharField(max_length=100, blank=True)
    release_date = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    video = models.BooleanField(default=False, blank=True)
    vote_average = models.FloatField(blank=True)
    vote_count = models.IntegerField(blank=True)
