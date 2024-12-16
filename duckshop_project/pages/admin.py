from django.contrib import admin

from .models import Product, CartEntry, OrderEntry, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(CartEntry)
admin.site.register(OrderEntry)
admin.site.register(Order)