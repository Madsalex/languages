from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *


def index(request):
    news = Article.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'index.html', {'news': news})


def article(request, id):
    item = Article.objects.get(pk=id)
    return render(request, 'article.html', {'item': item})


def create(request):
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
    return render(request, 'create_article.html', {'form': form})
