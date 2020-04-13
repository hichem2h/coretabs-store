from django.urls import path
from .views import product_list, product_details, add_product, edit_product


urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/new', add_product, name='add_product'),
    path('products/<pk>', product_details, name='product_details'),
    path('products/edit/<pk>', edit_product, name='edit_product'),
]
