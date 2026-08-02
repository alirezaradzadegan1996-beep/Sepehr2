
class ServiceManager:

    def start(self):

        return {
            "service": "sepehr_agent",
            "status": "started"
        }


    def stop(self):

        return {
            "service": "sepehr_agent",
            "status": "stopped"
        }


service_manager = ServiceManager()
