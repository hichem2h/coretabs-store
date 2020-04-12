from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    # We can use messages to notify user: "Email sent" or add email sent template

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
