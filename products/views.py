from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import AddProductForm


def product_list(request):

    # We can use Class based views like ListView
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_details.html', {'product': product})


def add_product(request):

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('add_product_success')
    else:
        form = AddProductForm()

    return render(request, 'products/add_product.html', {'form': form})


def add_product_success(request):
    return render(request, 'products/add_product_success.html')
