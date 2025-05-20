from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from shop.models import Product, Category


class AllCategoryView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'shop/all_category.html', {'categories': categories})

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


def about(request):
    return render(request, 'about.html')

class SearchView(View):
    def post(self, request, *args, **kwargs):
        searched = request.POST.get('searched', '')
        if searched:
            products = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
            if not products:
                messages.error(request, 'چنین محصولی یافت نشد')
            return render(request, 'shop/search.html', {'searched': products})
        else:
            messages.error(request, 'لطفا نام محصول را وارد کنید')
            return render(request, 'shop/search.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'shop/product.html', {'product': product})


class CategoryView(View):
    def get(self, request, str):
        cat = str.replace('_', ' ')
        try:
            category = Category.objects.get(name=cat)
            products = Product.objects.filter(category=category)
            return render(request, 'shop/category.html', {'products': products, 'category': category})
        except:
            messages.error(request, 'Category does not exist')
            return redirect('shop:home')
