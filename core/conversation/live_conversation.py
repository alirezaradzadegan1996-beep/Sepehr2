
class LiveConversation:

    def process(self, text):

        return {
            "input": text,
            "intent": "understood",
            "response": "generated_response",
            "status": "CONVERSATION_ACTIVE"
        }


live_conversation = LiveConversation()
