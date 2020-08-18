from django.shortcuts import render, redirect, Http404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib import messages

from .forms import SignupForm
from .models import Account

# Create your views here.

def login(request):
    if request.method == 'GET':
        form = LoginForm()
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
        form = SignupForm()
        return render(request, 'accounts/signup.html', context={'form' : form})

    post = request.POST
    form = SignupForm(post)

    if Account.objects.filter(username=post['username']).count() > 0:
        messages.warning(request, "account with the same username is already exists!")
        print("account saved")
    else:
        if form.validate_password():
            form.save()
            messages.success(request, "Account has been added")
        else:
            messages.warning(request, "passwords don't match! {} {}".format(post["password1"], post["password2"]))

    return redirect("signup")