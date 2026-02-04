from django.urls import path
from news.views import news, single_news, category_detail, search, register
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('', news, name='news'),
    path('single_news/<slug:slug>/', single_news, name='single_news'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('search', search, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]