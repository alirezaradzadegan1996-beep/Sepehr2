
class ResponseConnector:

    def connect(self):
        return {
            "response":"linked",
            "status":"RESPONSE_PIPELINE_CONNECTOR_ACTIVE"
        }

response_connector=ResponseConnector()
