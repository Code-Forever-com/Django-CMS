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

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['created_time']
    search_fields = ['name']
    prepopulated_fields={'slug':('name',)}
    class Meta:
        model = Category

admin.site.register(Category,CategoryAdmin)

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['post','cat']
    search_fields = ['cat']
    class Meta:
        model = PostCategory

admin.site.register(PostCategory,PostCategoryAdmin)

class LabelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['created_time']
    search_fields = ['name']
    prepopulated_fields={'slug':('name',)}
    class Meta:
        model = Label

admin.site.register(Label,LabelAdmin)

class PostLabelAdmin(admin.ModelAdmin):
    list_display = ['post','label']
    search_fields = ['label']
    class Meta:
        model = PostLabel

admin.site.register(PostLabel,PostLabelAdmin)

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

