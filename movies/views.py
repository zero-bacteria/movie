from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse, HttpResponse
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm
import random
import requests


API_KEY = 'e47b8bdb13776037d1c67d018b9cfac3'
API_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR'
response = requests.get(API_URL).json()

# Create your views here.
@require_GET
def index(request):
    movies = response
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(response, movie_pk)
    reviews = Review.objects.order_by('-pk')

    context = {
        'movie': movie,
        'reviews': reviews,
    }
    return render(request, 'movies/detail.html', context)

@require_http_methods(['GET', 'POST'])
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('movies:review_detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/review_create.html', context)

@require_GET
def reveiw_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/review_detail.html', context)

@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)

@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
            'count' : review.like_users.count(),
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)


@require_GET
def recommended(request):
    movies = Movie.objects.order_by('?')[:10]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/recommended.html', context)
