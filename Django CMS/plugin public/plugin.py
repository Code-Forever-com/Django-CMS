
#plugin api
class PluginAPI():
    def register(self):
        meta = {}
        for meta_key in self.Meta.__dict__:
            if not(meta_key.startswith("__") or callable(meta_key)):
                meta[meta_key] = self.Meta.__dict__[meta_key]
        plugin = self.save2db(meta)

        if "Option" in self.__class__.__dict__:
            option = {}
            for option_key in self.Option.__dict__:
                if not(option_key.startswith("__") or callable(option_key)):
                    option[option_key] = self.Option.__dict__[option_key]
            self.save2dboptions(plugin,option)
       
    def createTab(self,tab_name,parent_tab = ""):
        if parent_tab != "":
            print(tab_name+" added as subtab.")
        else:
            print(tab_name+" added as parenttab.")

    @classmethod
    def save2db(self,meta = {}):
        plugin_name = ""
        plugin_description = ""
        folder_name = "plugin"
        main_file = "main.py"
        if "plugin_name" in meta:
            plugin_name = meta["plugin_name"]
        if "plugin_description" in meta:
            plugin_description = meta["plugin_description"]
        if "folder_name" in meta:
            folder_name = meta["folder_name"]
        if "main_file" in meta:
            main_file = meta["main_file"]

        print(plugin_name+" saved." + plugin_description + " " + folder_name +" " + main_file)
        return plugin_name

    @classmethod
    def save2dboptions(self,plugin,options = {}):
        key_list = list(options["options"].keys())
        for key in key_list:
            print(key+" sets for " + options["options"][key])

    

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




#decorators


func_list = []

def post_save(function):
    func_list.append(function)
            



@post_save
def x(z):
    print(z)


