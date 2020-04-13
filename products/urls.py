from django.urls import path
from .views import product_list, product_details, add_product, edit_product


urlpatterns = [
    path('', product_list, name='product_list'),
    path('new', add_product, name='add_product'),
    path('<pk>', product_details, name='product_details'),
    path('edit/<pk>', edit_product, name='edit_product'),
]
