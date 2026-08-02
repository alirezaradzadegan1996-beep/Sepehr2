

class APIConnector:


    def connect(self, service):

        return {

            "api":
                service,

            "authentication":
                "completed",

            "communication":
                "active",

            "status":
                "EXTERNAL_API_INTEGRATION_ACTIVE"

        }



api_connector = APIConnector()

