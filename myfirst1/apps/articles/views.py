from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment, Alfa_Romeo


def index(request):
    a = len(Article.objects.all())
    b = int(a-3)
    latest_articles_list = Article.objects.all()[b:]
    return render(request, "articles/list.html", {'latest_articles_list': reversed(latest_articles_list)})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    return render(request, 'articles/detail.html', {'article': a})


def car_alfa(request):
    all_cars = Alfa_Romeo.objects.all()
    return render(request, 'articles/list_alfa_romeo.html', {'all_cars': all_cars})


def ar_145(request, article_id):
    try:
        a = Article.objects.get(id= article_id)
    except:
        raise Http404('Статья не найдена')

    return render(request, 'articles/news_opened.html', {'article': a})


def car(request, car_id):
    try:
        a = Alfa_Romeo.objects.get(id= car_id)
    except:
        raise Http404('Статья не найдена')

    return render(request, 'articles/car_detail.html', {'car': a})
