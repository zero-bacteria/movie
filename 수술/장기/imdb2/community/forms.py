from django import forms
from .models import Article, CATEGORY, ArticleComment


class ArticleForm(forms.ModelForm):
    cate = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(), required=True)
    
    class Meta:
        model = Article
        fields = ['cate', 'title', 'content']


class ArticleCommentForm(forms.ModelForm):

    class Meta:
        model = ArticleComment
        exclude = ['article', 'user']
