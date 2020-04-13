from django.urls import path

from .views import cart, add_to_cart, remove_from_cart, clear_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<product_id>', add_to_cart, name='add_to_cart'),
    path('remove/<product_id>', remove_from_cart, name='remove_from_cart'),
    path('clear', clear_cart, name='clear_cart'),
]
