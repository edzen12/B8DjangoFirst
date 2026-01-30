from django.shortcuts import render, get_object_or_404
from news.models import News, Category, Comment
from django.db.models import Q
from news.forms import CommentForm 
from django.shortcuts import redirect


def search(request):
    query = request.GET.get('q', '')
    category_all = Category.objects.filter(news__isnull=False).distinct()
    results = []

    if query:
        results = News.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    context = {
        'query':query,
        'results':results,
        'category_all':category_all,
    }
    return render(request, 'pages/search.html', context)

def news(request):
    news_all = News.objects.all()
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'category_all':category_all,
        'news_all': news_all,
    }
    return render(request, 'news.html', context)

def single_news(request, slug):
    news = get_object_or_404(News, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct()
    comments = news.comments.filter(is_published=True).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('pages/single_news', slug=slug)
    else:
        form=CommentForm()

    context = {
        'category_all': category_all,
        'news': news,
        'comments':comments,
        'form':form
    }
    return render(request, 'pages/single-news.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct()
    news = News.objects.filter(category=category) # Фильтруем посты по категории
    context = {
        'category': category,
        'category_all': category_all,
        'news': news,
    }
    return render(request, 'pages/category_detail.html', context)