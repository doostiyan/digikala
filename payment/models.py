from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShopingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoping_full_name = models.CharField(max_length=200)
    shoping_email = models.EmailField(blank=True, null=True)
    shoping_phone_number = models.CharField(max_length=11)
    shoping_address = models.TextField()
    shoping_city = models.CharField(max_length=200)
    shoping_state = models.CharField(max_length=200)
    shoping_zip_code = models.CharField(max_length=200, blank=True, null=True)
    shoping_country = models.CharField(max_length=200)
    shoping_old_cart = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'shoping address'
        verbose_name_plural = 'shoping addresses'

    def __str__(self):
        return f"{self.shoping_full_name}"
    