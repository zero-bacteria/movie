from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Theater, Comment
from .forms import TheaterForm, CommentForm


@require_GET
def index(request):
    theaters = Theater.objects.order_by('-pk')
    context = {
        'theaters': theaters,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = TheaterForm(request.POST) 
        if form.is_valid():
            theater = form.save(commit=False)
            theater.user = request.user
            theater.save()
            return redirect('community:detail', theater.pk)
    else:
        form = TheaterForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, theater_pk):
    theater = get_object_or_404(Theater, pk=theater_pk)
    comments = theater.comment_set.all()
    comment_form = CommentForm()
    context = {
        'theater': theater,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, theater_pk):
    theater = get_object_or_404(Theater, pk=theater_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.theater = theater
        comment.user = request.user
        comment.save()
        return redirect('community:detail', theater.pk)
    context = {
        'comment_form': comment_form,
        'theater': theater,
        'comments': theater.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, theater_pk):
    if request.user.is_authenticated:
        theater = get_object_or_404(Theater, pk=theater_pk)
        user = request.user

        if theater.like_users.filter(pk=user.pk).exists():
            theater.like_users.remove(user)
            liked = False
        else:
            theater.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
            'count' : theater.like_users.count(),
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)
