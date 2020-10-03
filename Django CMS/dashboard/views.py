from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from post.models import *
#from ui.ui import UI 
from django.contrib.admin.sites import site
from django.utils.text import capfirst
from django.urls import NoReverseMatch, reverse
from django.apps import apps

from .models import BlogOption

def get_blog_option(key):
    return BlogOption.objects.filter(blog_key=key).first() or "Djangos"


class DashboardView():
    #blog options
    site_title = "{} Dashboard".format(get_blog_option("blog_name"))
    index_title = "Djangos"


    #templates
    home_template = "admin/dashboard.html"
    login_template = "admin/login.html"
    register_template = "admin/register.html"

    post_type_index_template = "admin/index.html"
    app_index_template = "admin/app_index.html"
    model_index_template = "admin/index.html"
    model_add_template = "admin/model_add.html"
    model_update_template = "admin/model_add.html"

    form_template = "admin/form.html"


    apps_admins_dict = site._registry.items()

    def get_app_list(self,request,label=None):
        app_dict = {}
        for(model,model_admin) in self.apps_admins_dict:
            app_label = model._meta.app_label

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            model_dict = {
                'name': capfirst(model._meta.verbose_name),
                'object_name': model._meta.object_name,
                'perms': perms,
                'admin_url': None,
                'add_url': None,
            }
            if perms.get('change') or perms.get('view'):
                model_dict['view_only'] = not perms.get('change')
                try:
                    model_dict['admin_url'] = reverse('dashboard:%s_%s_index' % info)
                except NoReverseMatch:
                    pass
            if perms.get('add'):
                try:
                    model_dict['add_url'] = reverse('dashboard:%s_%s_add' % info)
                except NoReverseMatch:
                    pass

            if app_label in app_dict:
                app_dict[app_label]['models'].append(model_dict)
            else:
                app_dict[app_label] = {
                    'name': apps.get_app_config(app_label).verbose_name,
                    'app_label': app_label,
                    'app_url': reverse(
                        'dashboard:app_list',
                        kwargs= {"app_label" : app_label}
                    ),
                    'has_module_perms': has_module_perms,
                    'models': [model_dict],
                }

        if label:
            return app_dict.get(label)
        return app_dict

    def postTypeIndexView(self,request,posttype_id):
        posts = Post.objects.filter(post_type=posttype_id)
        postType = PostType.objects.filter(id=posttype_id).first()
        
        context = {
                'post_type_info': postType,
                "posts":posts,
                **self.get_nav_list(request),
            }
        return render(request, self.post_type_index_template ,context)


    def get_nav_list(self,request):
        app_list = self.get_app_list(request)
        app_list_keys = app_list.keys()
        new_app_list = []
        plugin_dict = {}
        user_dict = {}
        for app_keys in app_list_keys:
            if not app_list[app_keys]['name'] in ['Account','Authentication and Authorization','Plugin','Post']:
                new_app_list.append(app_list[app_keys])
            elif app_list[app_keys]['name'] == 'Plugin':
                plugin_dict = app_list[app_keys]
            elif app_list[app_keys]['name'] == 'Authentication and Authorization':
                user_dict = app_list[app_keys]
            else:
                continue 
            
        posttype_list = PostType.objects.all()

        return {
            'app_list': new_app_list,
            'plugin_dict': plugin_dict,
            'posttype_list':posttype_list,
            'user_dict':user_dict,
            }

    def index(self,request,extra_context=None):
        context = { 
            # **self.each_context(request),
            'title': self.index_title,
            **self.get_nav_list(request),
            **(extra_context or {}),
        }
        return render(request,self.home_template,context)

    def login(self,request,extra_context=None):
        if request.POST:
            post = request.POST
            username = post["username"]
            password = post["password"]
            user = authenticate(username=username,password=password)
            if user:
                messages.success(request,"Login is successfully!","cms-alert cms-alert-success")
                login(request,user)
                return redirect("dashboard:index")
            else:
                messages.error(request,"Login is not successfully!","cms-alert cms-alert-error")
                return render(request,"admin/login.html")
        else:
            return render(request,"admin/login.html")

    def app_index(self,request,app_label=""):
        app_dict = self.get_app_list(request,app_label)
        if not app_dict:
            raise Http404('The requested admin page does not exist.')
        # Sort the models alphabetically within each app.
        app_dict['models'].sort(key=lambda x: x['name'])
        app_name = apps.get_app_config(app_label).verbose_name
        context = {
            # **self.each_context(request),
            'title': '%(app)s administration' % {'app': app_name},
            'curr_app_list': [app_dict],
            'curr_app_label': app_label,
            **self.get_nav_list(request),
        }

        return render(request,self.app_index_template ,context)


    def model_index(self,request):
        return HttpResponse("hello")

    def model_add(self,request):
        return HttpResponse("hello")
        

    def model_autocomplete(self,request):
        return HttpResponse("hello")
        

    def model_update(self,request):
        return HttpResponse("hello")
        

    def model_delete(self,request):
        return HttpResponse("hello")
        

    def model_history(self,request):
        return HttpResponse("hello")
        

dashboard_view = DashboardView()