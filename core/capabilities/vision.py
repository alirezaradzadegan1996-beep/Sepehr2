
class VisionCapability:


    name = "vision"


    def can_handle(self,text):

        return "vision" in text



    def handle(self,text):

        return {
            "capability":"vision",
            "status":"active"
        }



capability = VisionCapability()
