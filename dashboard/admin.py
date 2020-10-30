from django.contrib import admin
from django.contrib.auth.models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ["name"]
    class Meta:
        model = Group 

        
admin.site.unregister(Group)
admin.site.register(Group,GroupAdmin)
