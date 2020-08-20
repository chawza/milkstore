from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as d_login

from .forms import SignupForm, LoginForm, UserLoginForm
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'accounts/login.html', context={'form': form})

    post = request.POST
    user = authenticate(request, username=post["username"], password=post['password'])
    
    if user is not None:
        d_login(request, user)
        return redirect('Store Home')
    else:
        #authenticate failed
        form = UserLoginForm(post)
        if form.is_exist():
            messages.error(request, "incorrext password")
        else:
            messages.error(request, "username does not exist!")
    return redirect('login')

    # if form.user_is_exist():
    #     # if user exist in db
    #     if form.login_correct():
    #         # go to store page
    #         user = authenticate(request, username=post["username"], password=post['password'])
    #         if user is not None:
    #             d_login(request, user)
    #             return redirect('home store')
    #         else:
    #             #authenticate failed
    #             messages.error(request, "dunno why, you can't login. ¯\\_(ツ)_/¯")
    #             return redirect('login')
    #     else:
    #         # password does not match with username
    #         messages.error(request, "password doesn't match!")
    # else: # username does not exist
    #     messages.error(request, "username doesn't exist in database!")
    # return redirect('login')

def signup(request):
    if request.method == 'GET':
        print(request.GET)
        form = SignupForm()
        return render(request, 'accounts/signup.html', context={'form' : form})

    post = request.POST
    form = SignupForm(post)

    if User.objects.filter(username=post['username']).count() > 0:
        messages.warning(request, "account with the same username is already exists!")
    else:
        if form.validate_password():
            form.save()
            messages.success(request, "Account has been added")
        else:
            messages.warning(request, "passwords don't match! {} {}".format(post["password1"], post["password2"]))

    return redirect("signup")