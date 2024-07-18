from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Customers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, default=' ', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='products/')
    stars = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=0)

    # SIZE_HA = (
    #     ('m', 32),
    #     ('l', 42),
    #     ('xl', 50),
    # )
    # size = models.CharField(max_length=4, choices=SIZE_HA, default='m')

    def __str__(self):
        return f'{self.name} {self.price} '


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=11,)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer} {self.product} {self.quantity}'

 