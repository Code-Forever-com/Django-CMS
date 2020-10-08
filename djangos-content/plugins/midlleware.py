import importlib

m = []
def importFiles(files=[]):
    for f in files:
        a = importlib.import_module("PluginAPI",f)
        m.append(a)

importFiles(["plugin public/plugin.py"])
print(m)