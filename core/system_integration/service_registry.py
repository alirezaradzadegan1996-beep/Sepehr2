

class ServiceRegistry:

    def register(self,service):
        return {
            "service":service,
            "status":"DYNAMIC_SERVICE_REGISTRY_ACTIVE"
        }


service_registry=ServiceRegistry()

