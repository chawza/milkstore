from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as d_login
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, LoginForm, UserLoginForm, EditProfile
from django.contrib.auth.models import User
from .models import UserDetail

# Create your views here.

def login(request):
    # response form page for login
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'accounts/login.html', context={'form': form})

    # get post request to authenticate User
    post = request.POST
    user = authenticate(request, username=post["username"], password=post['password'])
    
    # perform built in User class validation
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
    # return form for new user to Sign up
    if request.method == 'GET':
        print(request.GET)
        form = SignupForm()
        return render(request, 'accounts/signup.html', context={'form' : form})

    # add user to db from User form, and then return to signup page with a message
    post = request.POST    
    form = SignupForm(post)

    #determine if user is already in database
    if User.objects.filter(username=post['username']).count() > 0:
        messages.warning(request, "account with the same username is already exists!")
    else:
        if form.validate_password():
            form.save() # save the new user
            new_user = User.objects.get(username=post["username"])
             # as well as detail model that associate with the user
            new_detail = UserDetail.objects.create(user=new_user)
            new_detail.save()
            messages.success(request, "Account has been added")
            return redirect('login')
        else:
            messages.warning(request, "passwords don't match! {} {}".format(post["password1"], post["password2"]))

    return redirect("signup")

@login_required
def profile_home(request):
    user = User.objects.get(username=request.user.username)
    
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

@login_required
def profile_edit(request):
    user = User.objects.get(username=request.user.username)

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

@login_required
def delete_account(request):
    user = User.objects.get(username=request.user.username)
    user.delete()
    messages.success(request, 'Account has been deleted')
    return redirect('login')

@login_required
def logout_account(request):
    logout(request)
    return redirect('login')