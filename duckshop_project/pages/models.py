from django.conf import settings
from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class CartEntry(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='CartEntry'
    )
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='CartEntry'
        )

    def __str__(self):
        return self.customer.username
    
    def get_absolute_url(self):
        return reverse('cart_detail', args=[str(self.id)])
    
class Order(models.Model):
    customer = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='Order'
        )
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.customer.username
    
    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
    
class OrderEntry(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderentry'
    )

    def __str__(self):
        return self.customer.username
    
    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
    

