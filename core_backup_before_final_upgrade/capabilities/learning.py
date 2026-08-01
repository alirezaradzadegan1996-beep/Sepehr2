
class LearningCapability:


    name = "learning"


    def can_handle(self,text):

        return "learning" in text



    def handle(self,text):

        return {
            "capability":"learning",
            "status":"active"
        }



capability = LearningCapability()
