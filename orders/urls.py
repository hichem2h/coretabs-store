from django.urls import path

from .views import order

urlpatterns = [
    path('', order, name='order'),
]
