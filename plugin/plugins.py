from models import *

def save2db(plugin_name,plugin_description = "",folder_name = ""):
    plugin = Plugin(name=plugin_name,description=plugin_description,folder_name=folder_name)
    plugin.save()
    print(plugin_name+" saved.")
    return plugin

def save2dboptions(plugin,options = {}):
    key_list = list(options.keys())

    for key in key_list:
        plugin_option = PluginOption(plugin=plugin,key=key,value=options[key])
        plugin_option.save()
        print(key+" sets for " + options[key])

def post_save(function):
    func = function.__name__
    print(func)
    

class PluginAPI():
    def register(self):
        plugin = save2db(self.Meta.plugin_name,self.Meta.plugin_description,self.Meta.folder_name)
        save2dboptions(plugin,self.Option.options)

    def createTab(self,tab_name,parent_tab = ""):
        if parent_tab != "":
            print(tab_name+" added as subtab.")
        else:
            print(tab_name+" added as parenttab.")



class a(PluginAPI):
    class Meta:
        plugin_name = "My Plugin"
        plugin_description = "My Plugin Description"
        folder_name = "mypluginfolder"

    class Option:
        options = {
            "key1" : "value1",
            "key2" : "value2",

        }

b = a()
b.register()
b.createTab("My Tab")
@post_save
def x():
    pass

x()