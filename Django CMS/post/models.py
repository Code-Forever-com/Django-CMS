from django.db import models
from django.urls import reverse
from datetime import datetime

class Post(models.Model):
    def donot(self):
        return 0
    author = models.ForeignKey("auth.User",on_delete=donot,related_name="posts")
    title = models.CharField(max_length=80,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    excerpt = models.CharField(max_length=150,verbose_name="Özet")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")
    image = models.ImageField(verbose_name="Öne Çıkan Resim",null=True,blank=True)
    slug = models.SlugField(unique=True,max_length=100,verbose_name="Kalıcı Bağlantı")
    is_draft = models.BooleanField(verbose_name="is Draft",default=False)
    is_publish = models.BooleanField(verbose_name="is Publish",default=False)
    post_type = models.ForeignKey("post.PostType",verbose_name="Post Type",on_delete=donot,related_name="postsoftype")

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="Kategori İsmi")
    slug = models.SlugField(unique=True,max_length=30,verbose_name="Kategori Bağlantı")
    description = models.CharField(max_length=100,verbose_name="Kategori Açıklaması")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.name

class PostCategory(models.Model):
    post = models.ForeignKey("post.Post",on_delete=models.CASCADE,verbose_name="Post of Category",related_name="category")
    cat = models.ForeignKey("post.Category",on_delete=models.CASCADE,verbose_name="Category of Post") 

class Label(models.Model):
    name = models.CharField(max_length=20,verbose_name="Etiket İsmi")
    slug = models.SlugField(unique=True,max_length=30,verbose_name="Etiket Bağlantı")
    description = models.CharField(max_length=100,verbose_name="Etiket Açıklaması")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.name

class PostLabel(models.Model):
    post = models.ForeignKey("post.Post",on_delete=models.CASCADE,verbose_name="Post of Label",related_name="label")
    label = models.ForeignKey("post.Label",on_delete=models.CASCADE,verbose_name="Label of Post") 

class Comment(models.Model):
    def donot(self):
        return 0
    post = models.ForeignKey("post.Post",on_delete=models.CASCADE,verbose_name="Post Comment",related_name="comments")
    comment = models.CharField(max_length=150,verbose_name="Comment Of Post")
    writer = models.ForeignKey("auth.User",on_delete=donot,related_name="comments")
    username = models.CharField(max_length=20,verbose_name="Username of Comment Writer",blank=True,null=True)
    email = models.EmailField(verbose_name="Email of Comment Writer",max_length=100,blank=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.username or self.writer

class PostType(models.Model):
    name = models.CharField(max_length=50,verbose_name="Name Of Post Type")
    description = models.CharField(max_length=150,verbose_name="Description Of Post Type")
    singular_name = models.CharField(max_length=50,verbose_name="Singlar Name Of Post Type")
    all_items = models.CharField(max_length=50,verbose_name="Label Of All Items Of Post Type")
    view_item = models.CharField(max_length=50,verbose_name="Label Of View Item Of Post Type")
    add_new_item = models.CharField(max_length=50,verbose_name="Label Of Adding New Item Of Post Type")
    add_new = models.CharField(max_length=50,verbose_name="Label Of Adding New Of Post Type")
    edit_item = models.CharField(max_length=50,verbose_name="Label Of Editing Item Of Post Type")
    not_found = models.CharField(max_length=50,verbose_name="Label Of Not Found Of Post Type")
    update_item = models.CharField(max_length=50,verbose_name="Label Of Updating Item Of Post Type")
    search_items = models.CharField(max_length=50,verbose_name="Label Of Searching Items Of Post Type")

    def __str__(self):
        return self.name
    

