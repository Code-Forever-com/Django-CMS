from django.db import models

class Plugin(models.Model):
    name = models.CharField(verbose_name="Name Of Plugin",max_length=50)
    description = models.CharField(verbose_name="Description Of Plugin",max_length=150)
    folder_name = models.CharField(verbose_name="Folder Name Of Plugin",max_length=50,default="plugin")
    status = models.BooleanField(verbose_name="Statue Of Plugin",default=False)
    main_file = models.CharField(verbose_name="Main File Name Of Plugin",default="main.py",max_length=20)
    
    def __str__(self):
        return self.name

class PluginOption(models.Model):
    plugin = models.ForeignKey(Plugin,verbose_name="Plugin",on_delete=models.CASCADE,related_name="options")
    key = models.CharField(verbose_name="Key Of Plugin Option",max_length=50)
    value = models.CharField(verbose_name="Value Of Plugin Option",max_length=150)

    def __str__(self):
        return self.key


