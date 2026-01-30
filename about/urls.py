from django.urls import path 
from about.views import about, staff, single_staff

urlpatterns = [ 
    path('', about, name="about"),
    path('staff/', staff, name="staff"),
    path('staff/<slug:slug>/', single_staff, name="single_staff"),
]