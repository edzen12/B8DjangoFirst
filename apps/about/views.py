from django.shortcuts import render, get_object_or_404
from apps.about.models import About, Staff
from apps.news.models import Category


def about(request):
    about = About.objects.latest('-id')
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'category_all':category_all,
        'about':about,
    }
    return render(request, 'pages/about.html', context)


def staff(request):
    staffs = Staff.objects.prefetch_related('sociallink_set')
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'category_all':category_all,
        'staffs':staffs,
    }
    return render(request, 'pages/staffs.html', context)



def single_staff(request, slug):
    staff = get_object_or_404(Staff, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct() 

    context = {
        'category_all': category_all,
        'staff': staff, 
    }
    return render(request, 'pages/single-staff.html', context)
