from core.memory.experience_memory import experience_memory
from core.memory.experience_normalizer import experience_normalizer


class ConversationMemoryBridge:

    def save(self, experience):

        data = {
            "goal": "unknown",
            "input": "unknown",
            "skill": "conversation",
            "success": True,
            "response": None,
            "source": "conversation_runtime"
        }


        if isinstance(experience, dict):

            context = experience.get("context", {})

            if isinstance(context, dict):

                text = context.get("input")

                if text:
                    data["goal"] = text
                    data["input"] = text


            response = experience.get("response")

            if isinstance(response, dict):

                data["response"] = response.get(
                    "response"
                )

            elif isinstance(response, str):

                data["response"] = response


        normalized = experience_normalizer.normalize(
            data
        )

        experience_memory.save(
            normalized
        )


        return {
            "experience": normalized,
            "memory": "saved",
            "status": "stored"
        }


conversation_memory_bridge = ConversationMemoryBridge()
