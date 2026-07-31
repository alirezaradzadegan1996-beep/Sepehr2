
class BatteryAnalysisCapability:


    name = "battery_analysis"


    def can_handle(self, text):

        return "battery_analysis" in text



    def handle(self, text):

        return {
            "capability": "battery_analysis",
            "message": "new capability created"
        }



capability = BatteryAnalysisCapability()
