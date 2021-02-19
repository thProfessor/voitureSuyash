from django.shortcuts import render, HttpResponse
from . models import Product
from math import ceil


def index(request):
    return render(request, 'index.html')


def model(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) + (n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        1, nSlides), 'product': products}
    return render(request, 'base.html', params)


def pricing(request):
    return HttpResponse("this is pricing page")
