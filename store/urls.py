from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def home(request):
    return redirect('product_list')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
