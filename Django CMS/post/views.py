from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Q


def get_posts(post_filter = {}):
    posts = Post.objects.all()

    # search section
    if 's' in post_filter:
        posts = Post.objects.filter(Q(title=post_filter['s'],content=post_filter['s']))
        return posts

    # author section
    if 'author' in post_filter:
        posts = posts.filter(author=post_filter['author'])

    elif 'author_name' in post_filter:
        user = User.objects.filter(username=post_filter['author_name'])
        posts = posts.filter(author=user.id)

    # post type section    
    if 'post_type' in post_filter:
        pt = PostType.objects.filter(singular_name=post_filter['post_type'])
        posts = posts.filter(post_type=pt.id)

    # status section
    if 'post_status' in post_filter:
        if 'publish' == post_filter['post_status']:
            posts = posts.filter(is_publish=True)
        elif 'draft' == post_filter['post_status']:
            posts = posts.filter(is_draft=True)

    # category section
    if 'cat' in post_filter:
        category = PostCategory.objects.filter(cat=post_filter['cat'])
        p_list = []
        for c in category:
            p = posts.filter(id=c.post.id).first()
            p_list.append(p)
        posts = p_list

    elif 'category_name' in post_filter:
        category = Category.objects.filter(name=post_filter['category_name']).first()
        category = PostCategory.objects.filter(cat=category.id)
        p_list = []
        for c in category:
            p = posts.filter(id=c.post.id).first()
            p_list.append(p)
        posts = p_list

    # tag section
    if 'tag' in post_filter:
        tag = Label.objects.filter(name=post_filter['tag']).first()
        tag = PostLabel.objects.filter(label=tag.id)
        p_list = []
        for t in tag:
            for p in posts:
                if p.id == t.post.id:
                    p_list.append(p)
        posts = p_list

    elif 'tag_id' in post_filter:
        tag = PostLabel.objects.filter(label=post_filter['tag_id'])
        p_list = []
        for t in tag:
            for p in posts:
                if p.id == t.post.id:
                    p_list.append(p)
        posts = p_list
    

    if 'posts_per_page' in post_filter:
        posts = Paginator(posts,post_filter['posts_per_page'])



    for p in posts:
        categories = PostCategory.objects.filter(post=p.id)
        labels = PostLabel.objects.filter(post=p.id)
        p.categories = list()
        p.labels = list()
        p.comments = Comment.objects.filter(post=p.id)
        for category in categories:
            cat = Category.objects.filter(id=category.cat.id)
            p.categories.append(cat)
        for label in labels:
            lab = Label.objects.filter(id=label.label.id)
            p.labels.append(lab)
            
    return posts

def get_post(post_id):
    p = Post.objects.filter(id=post_id).first()
    if p:
        categories = PostCategory.objects.filter(post=p.id)
        labels = PostLabel.objects.filter(post=p.id)
        p.categories = list()
        p.labels = list()
        p.comments = Comment.objects.filter(post=p.id)
        for category in categories:
            cat = Category.objects.filter(id=category.cat.id)
            p.categories.append(cat)
        for label in labels:
            lab = Label.objects.filter(id=label.label.id)
            p.labels.append(lab)

    return p

def get_post_author(postID):
    post = Post.objects.filter(id=postID).first()
    return post.author

def get_post_comments(postID):
    comments = Comment.objects.filter(post=postID)
    return comments