from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Profile
from .forms import *
from django.contrib import messages

def loginView(request): 
    if request.user.is_authenticated:
        return redirect("dashboard:index")

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None: 
            login(request,user)
            return redirect("dashboard:index")
        else:
            messages.error(request,"Login is not successfully!","cms-alert cms-alert-error")
    return render(request,"admin/login.html",{"form":form})

def registerView(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("account:login")
        
    return render(request,"admin/login.html",{"form":form})

def logoutView(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    else:
        logout(request)
        return redirect("account:login")
