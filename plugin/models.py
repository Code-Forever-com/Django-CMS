from django.db import models

class PluginOption(models.Model):
    key = models.CharField(verbose_name="Key Of Plugin Option",max_length=50)
    value = models.CharField(verbose_name="Value Of Plugin Option",max_length=150)

    def __str__(self):
        return self.key


