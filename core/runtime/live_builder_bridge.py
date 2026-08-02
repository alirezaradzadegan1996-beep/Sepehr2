
class LiveBuilderBridge:

    def build(self, request):
        return {
            "request":request,
            "builder":"executed",
            "status":"completed"
        }

live_builder_bridge = LiveBuilderBridge()
