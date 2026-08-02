
from core.conversation.live_conversation_brain import live_conversation_brain
from core.conversation.conversation_memory_bridge import conversation_memory_bridge


class ConversationRuntime:

    def chat(self, text):

        meaning = live_conversation_brain.understand(text)

        response = live_conversation_brain.respond(
            meaning
        )

        memory = conversation_memory_bridge.save(
            response
        )

        return {
            "meaning": meaning,
            "response": response,
            "memory": memory,
            "status":"completed"
        }


conversation_runtime = ConversationRuntime()
