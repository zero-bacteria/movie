from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
# from django.db.models import Count
from django.conf import settings
import os
from PIL import Image

CATEGORY = [('INFO', '정보게시판'), ('HELP', '요청사항'), ('MARVEL', '마블극장'), ('TARANTINO', '타란티노극장'), ('NOLAN', '놀란극장'), ('KOREAN', '한국영화극장')]

def user_directory_path(instance, filename):
	article_pic_name = f'articles/{instance.title}.jpg'
	full_path = os.path.join(settings.MEDIA_ROOT, article_pic_name)

	if os.path.exists(full_path):
		os.remove(full_path)
	return article_pic_name


class Article(models.Model):
    notice = models.BooleanField(default=False, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cate = models.CharField(max_length=50, blank=True, choices=CATEGORY)
    views_count = models.IntegerField(default=0, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)

    # hate_users = models.ManyToManyField(User, related_name='hate_articles', blank=True)
    # image_link = models.TextField(default = '', blank=True)
    # youtube_link = models.TextField(default='', blank=True)
    

class ArticleComment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
