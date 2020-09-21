from django.contrib import admin
from .models import Profile,Settings

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user']
    class Meta:
        model = Profile

admin.site.register(Profile,UserModelAdmin) 

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['user']
    class Meta:
        model = Settings

admin.site.register(Settings,SettingsAdmin) 

