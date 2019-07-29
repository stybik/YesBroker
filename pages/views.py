from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import state_choices, price_choices, bedroom_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(id_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    #Get all realtors

    realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    print("Hello")
    print("New Hello")
    print("last try")
    print("wait for 15 mins")

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }


    return render(request, 'pages/about.html', context)
