class ServiceRegistry:

    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def get(self, name):
        return self.services.get(name)

    def has(self, name):
        return name in self.services

    def remove(self, name):
        self.services.pop(name, None)

    def list(self):
        return list(self.services.keys())

registry = ServiceRegistry()
