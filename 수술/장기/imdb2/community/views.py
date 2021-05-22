from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article, ArticleComment
from .forms import ArticleForm, ArticleCommentForm


@require_GET
def notice(request):
    articles = Article.objects.filter(cate='NOTICE').order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/info.html', context)

@require_GET
def info(request):
    articles = Article.objects.filter(cate='INFO').order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/info.html', context)

@require_GET
def marvel(request):
    articles = Article.objects.filter(cate='MARVEL').order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/marvel.html', context)

@require_GET
def tarantino(request):
    articles = Article.objects.filter(cate='TARANTINO').order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/tarantino.html', context)

@require_GET
def ticket_box(request):
    articles = Article.objects.filter(cate='TICKET_BOX').order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/ticket_box.html', context)
    
@require_GET
def korean(request):
    articles = Article.objects.filter(cate='KOREAN').order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/korean.html', context)

@require_GET
def nolan(request):
    articles = Article.objects.filter(cate='Nolan').order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/nolan.html', context)

@require_GET
def index(request):
    articles = Article.objects.order_by('-like_users')
    context = {
        'articles': articles,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('community:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = ArticleCommentForm()
    article.views_count += 1
    article.save()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = ArticleCommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('community:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': article.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, article_pk, mode=0):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        if mode and article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            liked = False
        else:
            if article.like_users.filter(pk=user.pk).exists():
                article.like_users.remove(user)
                liked = False
            else:   
                article.like_users.add(user)
                liked = True
                # hate(request, article_pk, 1)
        
        like_status = {
            'liked' , liked,
            'count' , article.like_users.count(),
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)




