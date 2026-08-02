
class ServiceLoader:
    def load(self):
        return {
            "services":"loaded",
            "status":"SERVICE_AUTO_LOADER_ACTIVE"
        }

service_loader=ServiceLoader()
