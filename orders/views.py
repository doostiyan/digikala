from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .cart import Cart
from shop.models import Order, Product


class OrderDetail(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()
        return render(request, 'orders/cart.html',
                      {'cart_products': cart_products, 'cart': cart, 'quantities': quantities, 'total': total})


class OrderAdd(View):

    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product, quantity=product_qty)

            cart_quantity = cart.__len__()

            response = JsonResponse({'qty': cart_quantity})
            messages.success(request, "سفارش شما اضافه شد")
            return response

# class OrderAdd(View):
#
#     def post(self, request):
#         cart = Cart(request)
#         if request.POST.get('action') == 'post':
#             product_id = request.POST.get('product_id')
#             if product_id:
#                 try:
#                     product_id = int(product_id)
#                     product = get_object_or_404(Product, id=product_id)
#                     cart.add(product=product)
#
#                     cart_quantity = cart.__len__()
#
#                     response = JsonResponse({'qty': cart_quantity})
#                     return response
#                 except ValueError:
#                     return JsonResponse({'error': 'Invalid product ID'}, status=400)
#             else:
#                 return JsonResponse({'error': 'No product ID provided'}, status=400)


class OrderUpdate(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            cart.update(product=product_id, quantity=product_qty)

            response = JsonResponse({'qty': product_qty})
            messages.success(request, "سفارش شما تغییر داده شد", 'info')
            return response


class OrderDelete(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))

            cart.delete(product=product_id)

            response = JsonResponse({'product': product_id})
            messages.error(request, "سفارش شما حذف شد", 'danger')
            return response