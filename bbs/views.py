from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        "message": "Welcome my BBS",
        "articles": articles,
    }
    return render(request, "bbs/index.html", context)


def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        "message": "Show Article " + str(id),
        "article": article,
    }
    return render(request, "bbs/detail.html", context)
