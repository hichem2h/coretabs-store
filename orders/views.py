from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .utils import send_order_email


@login_required
def order(request):
    user = request.user

    if not user.cart.items.exists():
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            order = form.save(user)
            send_order_email(user, order)
            return render(request, 'orders/order_success.html')
    else:
        form = OrderForm()

    return render(request, 'orders/order.html', {'form': form})
