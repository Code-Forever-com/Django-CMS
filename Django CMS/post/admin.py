from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time']
    list_filter = ['created_time']
    search_fields = ['title','content']
    prepopulated_fields={'slug':('title',)}
    class Meta:
        model = Post

admin.site.register(Post,PostAdmin)

class TermAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['created_time']
    search_fields = ['name']
    prepopulated_fields={'slug':('name',)}
    class Meta:
        model = PostTerm

admin.site.register(PostTerm,TermAdmin)

class PostTermAdmin(admin.ModelAdmin):
    list_display = ['post','term']
    search_fields = ['term']
    class Meta:
        model = PostTermStorage

admin.site.register(PostTermStorage,PostTermAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['writer']
    search_fields = ['comment','writer']
    class Meta:
        model = Comment

admin.site.register(Comment,CommentAdmin)

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name','description']
    class Meta:
        model = PostType

admin.site.register(PostType,PostTypeAdmin)

