from django.urls import path,include,re_path
from .views import dashboard_view



from django.contrib.admin.sites import site


app_name = "dashboard"

def addView(request):
    pass





def get_model_admin_urls(app_label,model_name):
    info = (app_label,model_name)

    return [
        path('', dashboard_view.model_index , name='%s_%s_index' % info),
        path('add/', dashboard_view.model_add, name='%s_%s_add' % info),
        path('autocomplete/', dashboard_view.model_autocomplete, name='%s_%s_autocomplete' % info),
        path('<path:object_id>/history/', dashboard_view.model_history, name='%s_%s_history' % info),
        path('<path:object_id>/delete/', dashboard_view.model_delete, name='%s_%s_delete' % info),
        path('<path:object_id>/update/',  dashboard_view.model_update, name='%s_%s_update' % info),
    ]






urlpatterns = [
  path('', dashboard_view.index, name='index'),
  path('login/', dashboard_view.login, name='login'),
  # path('logout/', logout, name='logout'),
    path("posts/<int:posttype_id>/", dashboard_view.postTypeIndexView,name="posttype_all_items"),
    path("posts/<int:posttype_id>/add/",dashboard_view.postTypeAddView,name="posttype_add_new_item"),
    path("posts/<int:posttype_id>/update/",dashboard_view.postTypeAddView,name="posttype_update_new_item"),
    path("posts/<int:posttype_id>/delete/",dashboard_view.postTypeAddView,name="posttype_delete_new_item"),
    

]

valid_app = []
for (model,modelAdmin) in site._registry.items():
    model_admin_urls = get_model_admin_urls(model._meta.app_label, model._meta.model_name)
    urlpatterns += [
      

      path('%s/%s/' % (model._meta.app_label, model._meta.model_name),include(model_admin_urls)),
    ]
    if not model._meta.app_label in valid_app:
        valid_app.append(model._meta.app_label)




if valid_app:
    regex = r'^(?P<app_label>' + '|'.join(valid_app) + ')/$'
    urlpatterns += [
        re_path(regex, dashboard_view.app_index, name='app_list'),
    ]




    