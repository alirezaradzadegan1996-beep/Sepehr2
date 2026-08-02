
class IntentBridge:

    def detect(self, message):
        return {
            "intent": "request",
            "message": message,
            "status": "detected"
        }

intent_bridge = IntentBridge()
