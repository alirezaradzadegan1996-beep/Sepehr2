

class IntentRuntime:

    def detect(self,text):
        return {
            "intent":"recognized",
            "status":"INTENT_RECOGNITION_RUNTIME_ACTIVE"
        }


intent_runtime=IntentRuntime()

