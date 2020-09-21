from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Profile,Settings



def loginView(request): 
    if request.user.is_authenticated:
        return redirect("post:profile",slug=request.user.username)

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None: 
            login(request,user)
            return redirect("post:profile",slug=username)
    return render(request,"login.html",{"form":form})

def registerView(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("account:login")
        
    return render(request,"account/register.html")

def logoutView(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    else:
        logout(request)
        return redirect("account:login")
