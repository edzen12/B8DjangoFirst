from django.shortcuts import render
from apps.contact.models import Contact


def contact_page(request):
    contacts = Contact.objects.latest('-id')
    context = {
        'contacts':contacts,
    }
    return render(request, 'pages/contact.html', context)