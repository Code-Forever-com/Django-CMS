from django.shortcuts import render,HttpResponse,redirect,Http404
from django.contrib.auth import authenticate,login
from django.contrib import messages
from post.models import *
from django.contrib.admin.sites import site
from django.utils.text import capfirst
from django.urls import NoReverseMatch, reverse
from django.apps import apps,AppConfig
from .models import BlogOption
from django.db.models.fields import *



def get_blog_option(key):
    return BlogOption.objects.filter(blog_key=key).first() or "Djangos"

site.disable_action("delete_selected")



def admin_login_required(function):
    def wrapper(DashboardView,request,*args,**kwargs):
        if request.user.is_superuser:
            return function(DashboardView,request,*args,**kwargs)
        else:
            return redirect("account:login")

    return wrapper
            



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

    plugin_header_tags = ["Plugin Name:","Plugin Description:","Plugin Author:","Plugin Author Url:","Plugin Website:","Plugin Version:"]



    def each_context(self):
        return {
            "site_title" : self.site_title,
            "index_title" : self.index_title,
        }


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

    @admin_login_required
    def postTypeIndexView(self,request,posttype_id):
        posts = Post.objects.filter(post_type=posttype_id)
        postType = PostType.objects.filter(id=posttype_id).first()
        
        model = apps.get_model("post","post")
        model_admin = self.get_modelAdmin(model)

        fields = []
        instance = model_admin.get_changelist_instance(request)

        for field in model_admin.list_display:
            try:
                fields.append( model._meta.get_field(field).verbose_name)
            except:
                pass
        
      

        result_list = []
        for result in instance.result_list:
            result_item = []
            
            for r in model_admin.list_display :
                result_item_dict = {}
                if not r.startswith("__"):
                    try:
                        result_item_dict["value"] = result.__dict__[r] 
                    except:
                        f = model._meta.get_field(r)
                        if f.related_model:
                            result_item_dict["value"] = f.related_model.objects.get(id=f.value_from_object(result)) 
                result_item.append(result_item_dict)
            
            result_list.append(result_item)

        instance.result_list = result_list 
        
        context = {
                'post_type_info': postType,
                "table":instance,
                "fields": fields,
                **self.get_nav_list(request),
            }
        return render(request, self.post_type_index_template ,context)
    
    @admin_login_required
    def postTypeAddView(self,request,posttype_id):
        return HttpResponse("post type add view %s" % posttype_id)
    
    @admin_login_required
    def postTypeUpdateView(self,request,posttype_id):
        return HttpResponse("post type update view %s" % posttype_id)

    @admin_login_required
    def postTypeDeleteView(self,request,posttype_id):
        return HttpResponse("post type delete view %s" % posttype_id)


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

    @admin_login_required
    def index(self,request,extra_context=None):
        context = { 
            **self.each_context(),
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

    @admin_login_required
    def app_index(self,request,app_label=""):
        app_dict = self.get_app_list(request,app_label)
        if not app_dict:
            raise Http404('The requested admin page does not exist.')
        # Sort the models alphabetically within each app.
        app_dict['models'].sort(key=lambda x: x['name'])
        app_name = apps.get_app_config(app_label).verbose_name

        if app_label == "plugin":
            plugin_list = self.plugin_index()
        else:
            plugin_list = False

        context = {
            # **self.each_context(request),
            'title': '%(app)s Administration' % {'app': app_name},
            'curr_app_list': [app_dict],
            'curr_app_label': app_label,
            **self.get_nav_list(request),
            'plugin_list': plugin_list
        }
      
        return render(request,self.app_index_template ,context)

    def get_model_label_from_req(self,request):
        path_list = request.get_full_path().split("/")
        return [path_list[2],path_list[3]]

    def get_modelAdmin(self,model):
        return site._registry[model]

    @admin_login_required
    def model_index(self,request):
        [app_label,model_label] = self.get_model_label_from_req(request)
        
        model = apps.get_model(app_label,model_label)
        model_admin = self.get_modelAdmin(model)

        fields = []
        instance = model_admin.get_changelist_instance(request)

        for field in model_admin.list_display:
            try:
                fields.append( model._meta.get_field(field).verbose_name)
            except:
                pass
        
      

        result_list = []
        for result in instance.result_list:
            result_item = []
            
            for r in model_admin.list_display :
                result_item_dict = {}
                if not r.startswith("__"):
                    try:
                        result_item_dict["value"] = result.__dict__[r] 
                    except:
                        f = model._meta.get_field(r)
                        if f.related_model:
                            result_item_dict["value"] = f.related_model.objects.get(id=f.value_from_object(result)) 
                result_item.append(result_item_dict)
            
            result_list.append(result_item)

        instance.result_list = result_list 
    
        context = {
            "model_label" : capfirst(model_label),
            **self.each_context(),
            **self.get_nav_list(request),
            "table" : instance,
            "fields" : fields,
            "model_perms" : model_admin.get_model_perms(request)
        }
        return render(request,self.model_index_template,context)

    @admin_login_required
    def model_add(self,request):
        
        [app_label,model_label] = self.get_model_label_from_req(request)
        model = apps.get_model(app_label,model_label)
        Form = self.generate_model_form(model)
        form = Form(request.POST or None)
        if model_label == "user":
            form.sort_user_fields(["username","first_name","last_name","email","is_superuser","groups","user_permissions","is_staff","password"])

        if form.is_valid():
            form.save()
            return redirect( "/dashboard/%s/%s/"%(app_label,model_label) )

        context = {
            **self.each_context(),
            **self.get_nav_list(request),
            "form" : form
        }
        
        return render(request,self.model_add_template,context)
        
    @admin_login_required
    def model_autocomplete(self,request):
        return HttpResponse("hello")
        
    @admin_login_required
    def model_update(self,request,object_id):
        [app_label,model_label] = self.get_model_label_from_req(request)
        model = apps.get_model(app_label,model_label)
        # generate form
        Form = self.generate_model_form(model)
        obj = model.objects.filter(id=object_id).first()
        
        form = Form(instance=obj)
        if model_label == "user":
            form.sort_user_fields(["username","first_name","last_name","email","is_superuser","groups","user_permissions","is_staff"])
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect( "/dashboard/%s/%s/"%(app_label,model_label) )

        context = {
            **self.each_context(),
            **self.get_nav_list(request),
            "form" : form
        }
        
        return render(request,self.model_add_template,context)
        
    @admin_login_required
    def model_delete(self,request,object_id):
        [app_label,model_label] = self.get_model_label_from_req(request)
        model = apps.get_model(app_label,model_label)
        
        obj = model.objects.filter(id=object_id).first()
        if obj:
            obj.delete()
            messages.success(request,"Model object was deleted successfully.","alert-success")
        else:
            messages.error(request,"Model object was not founded!","alert-danger")
        return redirect("/dashboard/%s/%s/"%(app_label,model_label))

    @admin_login_required
    def model_history(self,request,object_id):
        return HttpResponse("hello")
        
    def plugin_index(self):
        from os import listdir
        from os.path import isdir,join

        new_plugin_list = []
        for plugin in listdir("./djangos-content/plugins"):
            if isdir( "./djangos-content/plugins/%s" % plugin ) and not plugin.startswith("__"):
                plugin_dict = {}
                f = open("./djangos-content/plugins/%s/credentials.txt" % plugin,"r")
                header_lines = f.readlines()
                for header in header_lines:
                    for header_tags in self.plugin_header_tags:
                        if(header.startswith(header_tags)):
                            plugin_dict[ header_tags.split("Plugin ")[1].replace(":","").replace(" ","_").lower() ] = header.split(header_tags)[1]
                new_plugin_list.append(plugin_dict)

        return new_plugin_list

    def generate_model_form(self,model1,obj = None):
        from django import forms
        class Form(forms.ModelForm):
            class Meta:
                model = model1
                exclude = []
            
            def sort_user_fields(self,field_array=[]):
                new_order = {}
                for field in field_array:
                    new_order[field] = self.fields[field]
                self.fields = new_order
             
        return Form
                

dashboard_view = DashboardView()