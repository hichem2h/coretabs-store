from django.urls import path
from .views import product_list, product_details, add_product, add_product_success


urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/new', add_product, name='add_product'),
    path('products/new/success', add_product_success, name='add_product_success'),
    path('products/<pk>', product_details, name='product_details'),
]
