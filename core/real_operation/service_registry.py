

class ServiceRegistry:

    def register(self):
        return {
            "services":"registered",
            "status":"SERVICE_AUTO_REGISTRATION_ACTIVE"
        }


service_registry=ServiceRegistry()

