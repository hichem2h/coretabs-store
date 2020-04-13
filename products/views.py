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


# Add our own decorator for superuser_required
# better do add and edit product with django admin (customize admin)
def add_product(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return render(request, 'products/add_product_success.html')
        else:
            form = AddProductForm()

        return render(request, 'products/add_product.html', {'form': form})
    else:
        return redirect('product_list')


def edit_product(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product_to_edit = get_object_or_404(Product, pk=pk)

        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES, instance=product_to_edit)

            if form.is_valid():
                form.save()
                return render(request, 'products/add_product_success.html')
        else:
            form = AddProductForm(instance=product_to_edit)

        return render(request, 'products/add_product.html', {'form': form})
    else:
        return redirect('product_list')
