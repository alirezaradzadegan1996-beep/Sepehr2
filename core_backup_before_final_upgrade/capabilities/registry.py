class CapabilityRegistry:

    def __init__(self):
        self.capabilities = {}


    def register(self, name, handler):
        self.capabilities[name] = handler


    def get(self, name):
        return self.capabilities.get(name)


    def list(self):
        return list(self.capabilities.keys())


    def has(self, name):
        return name in self.capabilities


registry = CapabilityRegistry()
