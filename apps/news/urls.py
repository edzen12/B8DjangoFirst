from django.urls import path
from apps.news.views import (news, single_news, category_detail,
                         search, register, profile, create_news)
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('', news, name='news'),
    path('single_news/<slug:slug>/', single_news, name='single_news'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('search', search, name='search'),
    path('profile', profile, name='profile'),
    path('create-news/', create_news, name='create_news'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]