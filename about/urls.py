from django.urls import path 
from about.views import about, staff

urlpatterns = [ 
    path('', about, name="about"),
    path('staff/', staff, name="staff"),
]