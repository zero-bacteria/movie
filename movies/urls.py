from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended', views.recommended, name='recommended'),

    
    path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:movie_pk>/<int:review_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/<int:review_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/<int:review_pk>/like/', views.like, name='like'),

]
