

class ExternalConnector:

    def connect(self,source):
        return {
            "source":source,
            "data":"received",
            "status":"EXTERNAL_INTELLIGENCE_ACTIVE"
        }


external_connector=ExternalConnector()

