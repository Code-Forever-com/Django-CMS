from django.urls import path
from .views import *

app_name = "form"

urlpatterns = [
    path("",generate_form,name="index"),
]

