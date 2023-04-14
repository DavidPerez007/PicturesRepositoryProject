from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.db import IntegrityError

# Create your views here.


def home(request):
    if (request.method == 'GET'):
        context_dict = {
            # 'username': username
        }
        # TODO
    return render(request, 'index.html', context_dict)


def sign_up(request):
    if (request.method) == 'GET':
        context_dict = {
            'signup_form': UserCreationForm
        }
        return render(request, 'signup.html', context_dict)
    else:
        try:
            form = UserCreationForm(request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = User.objects.create_user(
                    username,
                    password
                    # email= request.POST['email']
                    # legal_age = request.POST['legal']
                    # ADD SOME OTHER FIELDS LIKE +18 AND EMAIL
                )
                user.save()
                login(request, user)
            context_dict = {
            'signup_form': UserCreationForm,
            'errors': form.errors.as_ul
            }
            return render(request, 'signup.html', context_dict)
        except IntegrityError:
            context_dict = {
            'signup_form': UserCreationForm,
            'errors': form.errors.as_ul
            }
            return render(request, 'signup.html', context_dict)


def log_in(request):
    if (request.method == 'GET'):
        context = {
            'form': AuthenticationForm
        }
        return render(request, 'logIn.html', context)
