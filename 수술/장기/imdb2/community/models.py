from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField


CATEGORY = [('INFO', '정보게시판'), ('TICKET_BOX', '매표소'), ('TARANTINO', '타란티노극장'), ('NOLAN', '놀란극장'), ('KOREAN', '한국영화극장')]

class Article(models.Model):
    notice = models.BooleanField(default=False, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, related_name='like_articles')
    hate_users = models.ManyToManyField(User, related_name='hate_articles')
    cate = models.CharField(max_length=50, blank=True, choices=CATEGORY)
    views_count = models.IntegerField(default=0, blank=True)
    # image_link = models.TextField(default = '', blank=True)
    # youtube_link = models.TextField(default='', blank=True)
    

class ArticleComment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
