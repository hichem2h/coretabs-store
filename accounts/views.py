from django.shortcuts import render, redirect
from django.utils.http import base36_to_int
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseBadRequest

from .forms import SignUpForm
from .tokens import confirm_email_token_generator
from .utils import send_cofirmation_email

User = get_user_model()


def signup(request):
    # We can use messages to notify user: "Email sent" instead of signup_success template

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # TODO dont save 2 times
            user.is_active = False
            user.save()
            send_cofirmation_email(request, user)
            return render(request, 'registration/signup_success.html')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def activate_email(request, uid, token):
    try:
        uid = base36_to_int(uid)
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        # Login automatically?
        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token')
