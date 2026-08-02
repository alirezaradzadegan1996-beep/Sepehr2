
class ContextBridge:

    def build(self, data):
        return {
            "context": data,
            "status": "built"
        }

context_bridge = ContextBridge()
