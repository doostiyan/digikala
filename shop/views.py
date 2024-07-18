from django.shortcuts import render

from shop.models import Products


def index(request):
    products = Products.objects.all()
    return render(request, 'shop/index.html', {'products': products})


def about(request):
    return render(request, 'about.html')
