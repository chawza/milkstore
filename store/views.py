from django.shortcuts import render
from django.http import HttpResponse

#import model from other apps
from django.apps import apps

# Create your views here.

def home(request):
    return render(request, 'store/home.html')