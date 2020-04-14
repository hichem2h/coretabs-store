from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
