from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    address = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price

        return total

    def __str__(self):
        return f'Order {self.id} by {self.user}'
