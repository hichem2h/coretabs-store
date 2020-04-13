from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('address',)

    def save(self, user):
        self.instance.user = user
        self.instance.save()

        for item in user.cart.items.all():
            self.instance.items.add(item)

        user.cart.items.clear()

        return self.instance
