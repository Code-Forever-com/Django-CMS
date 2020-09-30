from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from post.models import *
#from ui.ui import UI 

def loginView(request):
    if request.POST:
        post = request.POST
        username = post["username"]
        password = post["password"]
        user = authenticate(username=username,password=password)
        if user:
            messages.success(request,"Login is successfully!","cms-alert cms-alert-success")
            login(request,user)
            return redirect("dashboard:main")
        else:
            messages.error(request,"Login is not successfully!","cms-alert cms-alert-error")
            return render(request,"admin/login.html")
    else:
        return render(request,"admin/login.html")

def mainView(request):
    if request.user.is_superuser:
        context = {
            "ptypes" : get_posttypes(request)
        }
        return render(request,"admin/dashboard.html",context)
    else:
        messages.error(request,"You are not authorized!","cms-alert cms-alert-error")
        return redirect("dashboard:login")


def addView(request,posttype_id):
    pass

def postTypeIndexView(request,posttype_id):
    posts = Post.objects.filter(post_type=posttype_id)

    context = {
            "ptypes" : get_posttypes(request),
            "posts":posts
        }
    return render(request,"admin/post-index.html",context)


# utils functions
def get_posttypes(request):
    return PostType.objects.all()