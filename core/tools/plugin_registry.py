
class PluginRegistry:

    def __init__(self):

        self.plugins = {}


    def register(self, name, plugin):

        self.plugins[name] = plugin

        return {
            "plugin": name,
            "status": "registered"
        }


    def get(self, name):

        return self.plugins.get(name)


plugin_registry = PluginRegistry()
