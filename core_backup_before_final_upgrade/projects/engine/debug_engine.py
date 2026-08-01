
class DebugEngine:


    name = "debug_engine"


    def analyze(self, error):

        return {
            "status": "analyzed",
            "error": error
        }



debug_engine = DebugEngine()
