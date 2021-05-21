from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.review, name='review'),
    path('marvle/', views.marvle, name='marvle'),
    path('korean/', views.korean, name='korean'),
    path('nolan/', views.nolan, name='nolan'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/like/', views.like, name='like'),
]
