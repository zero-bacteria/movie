from django.db import models
from django.conf import settings


CATEGORY = [('Review', '영화리뷰'), ('Marvle', '마블관'), ('Nolan', '놀란관'), ('Korean', '한국영화관')]

class Article(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    rank = models.IntegerField(default=0, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_articles')
    cate = models.CharField(max_length=50, blank=True, choices=CATEGORY)
    views_count = models.IntegerField(default=0, blank=True)
    youtube_link = models.TextField(default='', blank=True)
    

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
