from django.urls import path
from apps.valuta.views import valuta_page


urlpatterns = [
    path('', valuta_page, name='valuta'),
]
