from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *


def index(request):
    news = Article.objects.filter(date__lte=timezone.now()).order_by('-date')[:2]
    return render(request, 'index.html', {'news': news})


def article(request, id):
    item = Article.objects.get(pk=id)
    return render(request, 'article.html', {'item': item})


def create(request):
    langs = Language.objects.all()
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CreateForm()
    return render(request, 'create_article.html', {'form': form, 'langs': langs})


def articles(request):
    news = Article.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'articles.html', {'news': news})


def map(request):
    return render(request, 'map.html')


def view_entries(request):
    group = request.GET.get('criteria')
    return render(request, 'list.html', {'entries': Article.objects.filter(language=group), 'group': group})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'articles.html')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'map.html')
