from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product

User = get_user_model()


# Through table to add quantity feature

# class CartItem(models.Model):
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price

        return total

    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
