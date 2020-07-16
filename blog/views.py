from django.shortcuts import render, get_object_or_404

from .models import Article

# Create your views here.


def blog(request):
    articles = Article.objects
    return render(request, 'blog/blog.html', {'articles': articles})


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article.html', {'article': article})
