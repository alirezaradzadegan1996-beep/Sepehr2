
class LiveActionChain:

    def execute(self, request):

        return {
            "request":request,
            "decision":"made",
            "action":"executed",
            "status":"completed"
        }

live_action_chain = LiveActionChain()
