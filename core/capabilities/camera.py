
class CameraCapability:


    name = "camera"


    def can_handle(self,text):

        return "camera" in text



    def handle(self,text):

        return {
            "capability":"camera",
            "status":"active"
        }



capability = CameraCapability()
