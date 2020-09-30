from django.contrib import admin
from django.contrib.admin import sites
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

class MyAdminSite(admin.AdminSite):
    site_header = 'DjangoS Dashboard'
    site_title = 'DjangoS Dashboard'
    index_template = 'admin/dashboard.html'

    def login(self,request,extra_context=None):
        if request.POST:
            post = request.POST
            username = post["username"]
            password = post["password"]
            user = authenticate(username=username,password=password)
            if user:
                messages.success(request,"Login is successfully!","cms-alert cms-alert-success")
                login(request,user)
                return redirect("admin:index")
            else:
                messages.error(request,"Login is not successfully!","cms-alert cms-alert-error")
                return render(request,"admin/login.html")
        else:
            return render(request,"admin/login.html")

admin_site = MyAdminSite(name='admin')
admin.site = admin_site
sites.site = admin_site