
class WeatherCapability:


    name = "weather"


    def can_handle(self,text):

        return "weather" in text



    def handle(self,text):

        return {
            "capability":"weather",
            "status":"active"
        }



capability = WeatherCapability()
