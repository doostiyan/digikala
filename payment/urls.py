from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment_success/', views.PaymentSuccessView.as_view(), name='payment_success'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
]


