from django import forms
from .models import Theater, Comment


class TheaterForm(forms.ModelForm):
    
    class Meta:
        model = Theater
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['theater', 'user']
