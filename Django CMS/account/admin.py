from django.contrib import admin
from .models import Profile

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user']
    class Meta:
        model = Profile

admin.site.register(Profile,UserModelAdmin) 



