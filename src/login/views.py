from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from login.forms import RegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect(reverse('login_register_success'))

    else:
        form = RegistrationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


def register_success(request):
    render(request, 'registration/success.html', {})
