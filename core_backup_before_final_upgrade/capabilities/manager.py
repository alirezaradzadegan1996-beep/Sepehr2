from core.capabilities import registry


class CapabilityManager:


    def list(self):

        return registry.list()


    def exists(self, name):

        return registry.has(name)


    def get(self, name):

        return registry.get(name)


    def info(self):

        return {
            "count": len(registry.list()),
            "capabilities": registry.list()
        }


manager = CapabilityManager()
