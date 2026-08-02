
class LiveConversationBrain:

    def understand(self, text):

        return {
            "input": text,
            "intent": "conversation",
            "status": "understood"
        }


    def respond(self, meaning):

        return {
            "response": "Sepehr ready",
            "context": meaning,
            "status": "generated"
        }


live_conversation_brain = LiveConversationBrain()
