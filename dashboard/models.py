from django.db import models

class BlogOption(models.Model):
    blog_key = models.CharField(max_length=50,verbose_name="Blog Key")
    blog_value = models.CharField(max_length=50,verbose_name="Blog Value")

