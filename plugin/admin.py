from django.contrib import admin
from .models import *

class PluginOptionAdmin(admin.ModelAdmin):
    list_display = ['key']
    class Meta:
        model = PluginOption

admin.site.register(PluginOption,PluginOptionAdmin)

