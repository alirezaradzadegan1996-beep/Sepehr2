
class LiveRouter:

    def route(self, request):
        return {
            "request":request,
            "intent":"detected",
            "status":"routed"
        }

live_router = LiveRouter()
