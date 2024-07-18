from django.conf.urls.static import static
from django.urls import path

from Digikala import settings
from shop import views

urlpatterns = [
    path('', views.index, name='index')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
