from django.contrib import admin
from .models import *

class FormsAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = Forms

admin.site.register(Forms,FormsAdmin) 

class FormFieldsAdmin(admin.ModelAdmin):
    list_display = ['title']
    class Meta:
        model = FormFields

admin.site.register(FormFields,FormFieldsAdmin) 

class FormFieldsStorageAdmin(admin.ModelAdmin):
    list_display = ['form','field']
    class Meta:
        model = FormFieldsStorage

admin.site.register(FormFieldsStorage,FormFieldsStorageAdmin) 
