from django.shortcuts import render
from django.views.generic import TemplateView
from django import views
from orders.cart import Cart
from .models import ShoppingAddress
from .forms import ShoppingForm
# Create your views here.
class PaymentSuccessView(TemplateView):
    template_name = 'payment/payment_success.html'

class CheckoutView(views.View):
    def get(self, request, ):
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()
        if request.user.is_authenticated:
            shopping_user = ShoppingAddress.objects.get(user__id=request.user.id)
            shopping_form = ShoppingForm(request.POST or None, instance=shopping_user)
            return render(request, 'payment/checkout.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shopping_form': shopping_form})
        else:
            shopping_form = ShoppingForm(request.POST or None)
            return render(request, 'payment/checkout.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shopping_form': shopping_form})

