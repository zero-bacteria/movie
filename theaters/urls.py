from django.urls import path
from . import views

app_name = 'theaters'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:theater_pk>/', views.detail, name='detail'),
    path('<int:theater_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:theater_pk>/like/', views.like, name='like'),
]
