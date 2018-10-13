from os import listdir
from os.path import isfile, join
import importlib
import sys

class PluginManager(object):

    def __init__(self):
        super(PluginManager, self).__init__()
        print "[+] Inititalizing plugins"
        self.plugins = {}
        self.loadPlugins()

    def loadPlugins(self):
        onlyfiles = (f for f in listdir("plugins") if f.endswith('.py'))
        sys.path.insert(0, "plugins")
        for f in onlyfiles:
            plugin = __import__(f[:-3]).Plugin()
            self.plugins[plugin.name] = plugin
            print "   [*] Plugin loaded: \"" + plugin.name + "\""

    def getPlugin(self, name):
        try:
            plugin = self.plugins[name]
            return plugin
        except KeyError:
            print "[!] The requested plugin \"" + name + "\" does not exist!"

    def executePlugin(self, name):
        if self.plugins[name] != nil :
            plugin.execute()
        else:
            print "[!] Plugin requested that does not exist"

    def close(self):
        for name in self.plugins:
            self.plugins[name].close()
