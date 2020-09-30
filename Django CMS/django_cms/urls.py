"""django_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path,include
from post.views import get_posts
from django.shortcuts import HttpResponse
from .admin import admin_site
def a(request):
    post = get_posts({"s":"a"})
    return HttpResponse(post)

urlpatterns = [
 #   path('admin/', admin.site.urls),

     path('dashboard/', admin_site.urls),
    path('account/',include("account.urls")),
    path('form/', include("form.urls")),
    path('abc/',a),
    path('', include("post.urls")),
    

]
