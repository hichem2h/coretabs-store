from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product

from .models import Cart


@login_required
def cart(request):
    return render(request, 'carts/cart.html', {'cart': request.user.cart})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.add(product)

    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.remove(product)

    return redirect('cart')


@login_required
def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.items.clear()

    return redirect('cart')
