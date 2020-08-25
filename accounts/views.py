from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as d_login

from .forms import SignupForm, LoginForm, UserLoginForm, EditProfile
from django.contrib.auth.models import User
from .models import UserDetail

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
            new_user = User.objects.get(username=post["username"])
            new_detail = UserDetail.objects.create(user=new_user)
            new_detail.save()
            messages.success(request, "Account has been added")
        else:
            messages.warning(request, "passwords don't match! {} {}".format(post["password1"], post["password2"]))

    return redirect("signup")

def profile_home(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not authenticated')
        redirect('login')
    try:
        user = User.objects.get(username=request.user.username)
    except user.DoesNotExist:
        messages.error(request, "can't find user in database")
        redirect('login')
    
    print(user.email, user.detail.cardnumber)
    
    context = {
        "user" : {
            "username" : user.username,
            "date" : user.date_joined,
            "email" : user.email,
            "cardnumber" : user.detail.cardnumber,
            'address' : user.detail.address,
        },
    }

    return render(request, 'accounts/profile.html', context=context)

def profile_edit(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not authenticated')
        redirect('login')
    try:
        user = User.objects.get(username=request.user.username)
    except user.DoesNotExist:
        messages.error(request, "can't find user in database")
        redirect('login')

    if request.method == 'GET':
        form = EditProfile()

        # form.fields['address'].widget.attrs['placeholder'] = user.detail.address
        # form.fields['cardnumber'].widget.attrs['placeholder'] = user.detail.cardnumber
        # form.fields['email'].widget.attrs['placeholder'] = user.email
        user = {
            'email' : user.email,
            'address' : user.detail.address,
            'cardnumber' : user.detail.cardnumber,
        }
        print(user)
        return render(request, 'accounts/profile_edit.html', {'user' : user})
    
    post = request.POST
    detail = user.detail
    detail.address = post['address']
    detail.cardnumber = post['cardnumber']
    user.email = post['email']
    
    detail.save()
    user.save()
    messages.success(request, "profile changes has been made")
    return redirect('profile')