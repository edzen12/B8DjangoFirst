from django.shortcuts import render
from about.models import About, Staff
from news.models import Category


def about(request):
    about = About.objects.latest('-id')
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'category_all':category_all,
        'about':about,
    }
    return render(request, 'pages/about.html', context)


def staff(request):
    staffs = Staff.objects.all()
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'category_all':category_all,
        'staffs':staffs,
    }
    return render(request, 'pages/staffs.html', context)

