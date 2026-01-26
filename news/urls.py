from django.urls import path
from news.views import news, single_news, category_detail, search

urlpatterns = [  
    path('', news, name='news'),
    path('single_news/<slug:slug>/', single_news, name='single_news'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('search', search, name='search'),
]