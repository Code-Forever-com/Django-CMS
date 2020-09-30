from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20,verbose_name="Menu Name")
    icon = models.CharField(max_length=50,verbose_name="İcon label")
    url = models.URLField(verbose_name="Menu URL")
    is_menu = models.BooleanField(verbose_name="is Menu",default=False)
    is_menu_item = models.BooleanField(verbose_name="is Menu Item",default=False)
    target = models.IntegerField(verbose_name="Target id",default=0)

    def __str__(self):
        return self.name


