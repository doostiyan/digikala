from django.contrib import admin

from shop import models

admin.site.register(models.Products)
admin.site.register(models.Customers)
admin.site.register(models.Orders)
admin.site.register(models.Category)
