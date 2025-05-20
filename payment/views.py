from django.shortcuts import render
from django.views.generic import TemplateView
from django import views
from orders.cart import Cart
from .models import ShopingAddress
from .forms import ShopingForm
# Create your views here.
class PaymentSuccessView(TemplateView):
    template_name = 'payment/payment_success.html'

class CheckoutView(views.View):
    def get(request, ):
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()
        if request.user.is_authenticated:
            shopping_user = ShopingAddress.objects.get(user__id=request.user.id)
            shopping_form = ShopingForm(request.POST or None, isinstance=shopping_user)
            return render(request, 'payment/checkout.html', {'cart_product': cart_products, 'quantities': quantities, 'total': total, 'shopping_form': shopping_form})
        else:
            shopping_form = ShopingForm(request.POST or None)
            return render(request, 'payment/checkout.html', {'cart_product': cart_products, 'quantities': quantities, 'total': total, 'shopping_form': shopping_form})
