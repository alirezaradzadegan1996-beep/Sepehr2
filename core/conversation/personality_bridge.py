
class PersonalityBridge:

    def apply(self,response):
        return {
            "personality":"sepehr",
            "response":response,
            "status":"applied"
        }

personality_bridge = PersonalityBridge()
