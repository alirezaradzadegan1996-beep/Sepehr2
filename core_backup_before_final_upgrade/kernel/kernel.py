class Kernel:

    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def get(self, name):
        return self.services.get(name)

    def boot(self):
        print("===================================")
        print("      Sepehr2 Kernel Boot")
        print("===================================")

        for name, service in self.services.items():
            if hasattr(service, "boot"):
                service.boot()

        print(f"Services Loaded: {len(self.services)}")
        print("Kernel Ready")
