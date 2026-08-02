from core.conversation.live_conversation_brain import live_conversation_brain
from core.conversation.conversation_memory_bridge import conversation_memory_bridge


class ConversationRuntime:

    def process(self,
                text,
                memory_context=None,
                experiences=None):

        return self.chat(
            text,
            memory_context,
            experiences
        )

    def chat(self,
             text,
             memory_context=None,
             experiences=None):

        meaning = live_conversation_brain.understand(
            text,
            memory_context=memory_context,
            experiences=experiences
        )

        response = live_conversation_brain.respond(
            meaning
        )

        # Natural Response Layer
        if isinstance(response, dict):

            inner = response.get(
                "response"
            )

            if isinstance(inner, dict):

                solution = inner.get(
                    "solution"
                )

                if solution:
                    response["response"] = solution

        memory = conversation_memory_bridge.save(
            response
        )

        return {
            "meaning": meaning,
            "response": response,
            "memory": memory,
            "status": "completed"
        }


conversation_runtime = ConversationRuntime()
