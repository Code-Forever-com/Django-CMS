from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE,verbose_name="User Profile")
    bio = models.CharField(verbose_name="Bio",max_length=200,null=True,blank=True)
    profile_photo = models.ImageField(verbose_name="Profil Fotoğrafı",null=True,blank=True)
    website_url = models.URLField(verbose_name="Website URL",max_length=150,null=True,blank=True)
    lang = models.CharField(verbose_name="Language",max_length=10,null=True,blank=True)
    facebook_url = models.URLField(verbose_name="Facebook URL",max_length=150,null=True,blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL",max_length=150,null=True,blank=True)
    twitter_url = models.URLField(verbose_name="Twitter URL",max_length=150,null=True,blank=True)
    github_url = models.URLField(verbose_name="Github URL",max_length=150,null=True,blank=True)
    linkedin_url = models.URLField(verbose_name="Linkedin URL",max_length=150,null=True,blank=True)

    def __str__(self):
        return self.user.username

class Settings(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="User Settings")
    is_dark = models.BooleanField(verbose_name="Karanlık Mod",default=False)

    def __str__(self):
        return self.user.username





