from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from . import accounts_form
from .models import Account

# Create your views here.

def login(request):
    if request.method == 'GET':
        form = accounts_form.LoginForm()
        return render(request, 'accounts/login.html', context={'form': form, 'signup_link' : 'signup'})

    elif request.method == 'POST':
        try:
            user = Account.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'accounts/profile.html', {
                'username' : user.username,
                'create_account' : user.date_create
            })
        except ObjectDoesNotExist:
            return HttpResponse('invalid account id')

def signup(request):
    if request.method == 'GET':
        print(request.GET)
        form = accounts_form.SignupForm()
        return render(request, 'accounts/signup.html', context={'form' : form})

    elif request.method == 'POST':
        new_account = Account(
            username=request.POST['username'],
            password=request.POST['password'],
            date_create=timezone.now()
        )

        new_account.save()
        print('account added to db ' + str(new_account))
        return HttpResponse("Account Signup!")