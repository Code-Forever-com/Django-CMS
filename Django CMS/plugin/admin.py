from django.contrib import admin
from .models import *

class PluginAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name','description']
    class Meta:
        model = Plugin

admin.site.register(Plugin,PluginAdmin)

class PluginOptionAdmin(admin.ModelAdmin):
    list_display = ['plugin','key']
    class Meta:
        model = PluginOption

admin.site.register(PluginOption,PluginOptionAdmin)