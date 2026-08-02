

class APIManager:

    def request(self,service):
        return {
            "service":service,
            "data":"received",
            "status":"EXTERNAL_API_MANAGER_ACTIVE"
        }


api_manager=APIManager()

