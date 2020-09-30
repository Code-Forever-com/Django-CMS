from django.urls import path
from .views import *

app_name = "dashboard"

urlpatterns = [
    path("login/",loginView,name="login"),
    path("index/",mainView,name="main"),
    path("type/<int:posttype_id>/add/",addView,name="posttype_add_new_item"),
    path("type/<int:posttype_id>/index/",postTypeIndexView,name="posttype_all_items"),
 #   path("users/",userIndexView,name="userIndex"),
  #  path("users/<int:userID>",userDetailView,name="userDetail")



]