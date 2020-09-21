from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def indexView(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list,5)
    page = request.GET.get('p')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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
    
    return render(request,"index.html",{"posts":posts})

def postView(request,slug):
    p = Post.objects.filter(slug=slug)
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
    
    return render(request,"index.html",{"post":p})

