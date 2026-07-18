class ServiceRegistry:

    def __init__(self):
        self.services = {}


    def register(self, name, service):

        if name in self.services:
            raise ValueError(
                f"Service '{name}' already registered."
            )

        self.services[name] = service


    def register_safe(self, name, service):

        if name not in self.services:
            self.services[name] = service

        return self.services[name]


    def unregister(self, name):

        if name in self.services:
            del self.services[name]


    def get(self, name):

        if name not in self.services:
            raise KeyError(
                f"Service '{name}' not found."
            )

        return self.services[name]


    def has(self, name):

        return name in self.services


    def list(self):

        return list(self.services.keys())


registry = ServiceRegistry()
