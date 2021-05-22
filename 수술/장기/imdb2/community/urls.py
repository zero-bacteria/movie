from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('info/', views.info, name='info'),
    path('marvel/', views.marvel, name='marvel'),
    path('korean/', views.korean, name='korean'),
    path('nolan/', views.nolan, name='nolan'),
    path('tarantino/', views.tarantino, name='tarantino'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/like/', views.like, name='like'),
]
