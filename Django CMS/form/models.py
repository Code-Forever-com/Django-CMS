from django.db import models

class Forms(models.Model):
    name = models.CharField(verbose_name="Form Name",max_length=50)
    slug = models.SlugField(verbose_name="Form Slug",max_length=50,default="")
    description = models.CharField(verbose_name="Form Description",max_length=15,null=True,blank=True)
    to_url = models.CharField(verbose_name="URL to ?",max_length=150)

    def __str__(self):
        return self.name

class FormFields(models.Model):
    title = models.CharField(verbose_name="Field Name",max_length=30)
    description = models.CharField(verbose_name="Field Description",max_length=50,null=True,blank=True)
    is_required = models.BooleanField(verbose_name="Is Required?",default=False) 
    field_type = models.CharField(verbose_name="Field Type",max_length=50)
    placeholder = models.CharField(verbose_name="Field Placeholder",max_length=50)
    custom_css = models.TextField(verbose_name="Field Custom CSS",null=True,blank=True)

    def __str__(self):
        return self.title

class FormFieldsStorage(models.Model):
    field = models.ForeignKey("form.FormFields",on_delete=models.CASCADE,verbose_name="Field")
    form = models.ForeignKey("form.Forms",on_delete=models.CASCADE,verbose_name="Form")

    def __str__(self):
        return self.form.name + "@" + self.field.title
    

