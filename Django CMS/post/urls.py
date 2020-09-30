from django.contrib import admin
from django.urls import path

from .views import *

app_name = "post"

urlpatterns = [
    path("",get_post,name="index"),
]
