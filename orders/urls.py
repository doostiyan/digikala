from django.urls import path

from orders import views
app_name = 'orders'
urlpatterns = [
    path('', views.OrderDetail.as_view(), name='order_details'),
    path('add/', views.OrderAdd.as_view(), name='order_add'),
    path('delete/', views.OrderDelete.as_view(), name='order_delete'),
    path('update/', views.OrderUpdate.as_view(), name='order_update'),
]