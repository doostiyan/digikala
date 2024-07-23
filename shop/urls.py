from django.conf.urls.static import static
from django.urls import path

from Digikala import settings
from shop import views
from shop.views import about
app_name = 'shop'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', about, name='about'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:str>/', views.CategoryView.as_view(), name='category'),
    path('category/', views.AllCategoryView.as_view(), name='all_category'),
]
