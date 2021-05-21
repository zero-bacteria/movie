from django import forms
from .models import Article, CATEGORY, Comment


class ArticleForm(forms.ModelForm):
    cate = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(), required=True)
    
    class Meta:
        model = Article
        fields = ['cate', 'title', 'content', 'youtube_link']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['article', 'user']
