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

    def get_categories(self):
        terms = self.terms.all()
        cat_terms = []
        for term in terms:
            if(term.term.is_category and term is not None):
                cat_terms.append(term.term)
        return cat_terms or False

    def get_labels(self):
        terms = self.terms.all()
        label_terms = []
        for term in terms:
            if(term.term.is_label and term is not None):
                label_terms.append(term.term)
        return label_terms or False
            
    def get_comments(self):
        return self.comments.all() or False

    def get_post_type(self):
        return self.post_type

    def get_permalink(self):
        return self.get_object_instances(["slug"])["slug"]

    def get_object_instances(self,field_array = []):
        instances = {}

        for field in field_array:
            try:
                instances[field] = self.__dict__[field]
            except:
                pass
        return instances



class PostTerm(models.Model):
    name = models.CharField(max_length=20,verbose_name="Kategori İsmi")
    slug = models.SlugField(unique=True,max_length=30,verbose_name="Kategori Bağlantı")
    description = models.CharField(max_length=100,verbose_name="Kategori Açıklaması")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")
    is_category = models.BooleanField(default=False,verbose_name="Is Category")
    is_label = models.BooleanField(default=False,verbose_name="Is Label")

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.name

class PostTermStorage(models.Model):
    post = models.ForeignKey("post.Post",on_delete=models.CASCADE,verbose_name="Post of Term",related_name="terms")
    term = models.ForeignKey("post.PostTerm",on_delete=models.CASCADE,verbose_name="Term of Post",related_name="termposts") 

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
