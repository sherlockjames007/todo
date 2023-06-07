# this file contains functions that return templates corresponding to different urls available in the project

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


# login function 
# checks if the user is already logged in or not
# if logged in redirect to home page if not log in user
# returns template for login page
def login(request):
    if request.user.is_authenticated:
        return redirect('base:home')
    page = 'login'
    context = {
        'page': page,
    }
    return render(request, 'base/login_register.html', context)


# register new user
# returns template for register page
def register(request):
    if request.user.is_authenticated:
        return redirect('base:home')
    page = 'register'
    context = {
        'page': page
    }
    return render(request, 'base/login_register.html', context)

# home page only available in case the user is logged in (login required)
# returns template for home page
@login_required
def home(request):    
    context = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return render(request, 'base/home_new.html', context)