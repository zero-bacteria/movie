from django import forms
from .models import Article, CATEGORY, ArticleComment


class ArticleForm(forms.ModelForm):
    cate = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(), required=True)
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = Article
        fields = ['cate', 'title', 'content', 'picture']


class ArticleCommentForm(forms.ModelForm):

    class Meta:
        model = ArticleComment
        exclude = ['article', 'user']
