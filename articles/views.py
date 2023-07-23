from django.shortcuts import render, HttpResponse
from articles.models import Articles, ArticlesCategory
from django.core.paginator import Paginator
import datetime
def home(reqests, page=1):
    articles = Articles.objects.all()
    paginator = Paginator(articles, 3)
    articles_paginator = paginator.page(page)
    context = {
        "title":"Home",
        "category": ArticlesCategory.objects.all(),
        "articles": articles_paginator,
        "top_3" : Articles.objects.order_by("-views")[:3],
        'date' : datetime.date.today()
    }

    return render(reqests, 'articles/home.html',context)

def archive(reqests, category_id=None):

    if category_id:
        category = ArticlesCategory.objects.get(id=category_id)
        articles = Articles.objects.filter(category=category)
    else:
        articles = Articles.objects.all()
    context = {
        "title": "Archive",
        "category": ArticlesCategory.objects.all(),
        'articles' : articles,
        "top_3": Articles.objects.order_by("-views")[:3],
        'date': datetime.date.today()
    }
    return render(reqests, "articles/archive.html", context)

def posts(reqests, pk):

    article = Articles.objects.get(id=pk)
    article.views = article.views + 1
    article.save()
    return render(reqests, 'articles/page.html', {'article':article, "top_3" : Articles.objects.order_by("-views")[:3], "category": ArticlesCategory.objects.all(),})