from core.memory.experience_memory import experience_memory
from core.memory.profile_memory import profile_memory
from core.cognitive.reasoning_bridge import reasoning_bridge


class LiveConversationBrain:

    def understand(
        self,
        text,
        memory_context=None,
        experiences=None
    ):

        return {
            "input": text,
            "intent": "conversation",
            "memory_context": memory_context,
            "experiences": experiences,
            "status": "understood"
        }


    def respond(self, meaning):

        text = meaning.get("input", "")

        memories = experience_memory.recall()["experiences"]


        # ==========================
        # Personal Memory
        # ==========================

        if "اسم من" in text and "است" in text:

            name = (
                text
                .replace("اسم من","")
                .replace("است","")
                .strip()
            )

            profile_memory.save(
                "name",
                name
            )

            experience_memory.save({
                "goal": text,
                "input": text,
                "skill":"conversation",
                "success":True,
                "source":"profile_memory",
                "response":None
            })

            response = f"خوشبختم {name}، به خاطر سپردم."


        elif "اسم من چی بود" in text or "اسمم چی بود" in text:

            name = profile_memory.get("name")

            if name:
                response = f"اسم شما {name} است."
            else:
                response = "هنوز اسم شما را نمی‌دانم."


        else:

            reasoning = reasoning_bridge.think(
                text
            )

            response = reasoning["solution"]


        return {
            "response": response,
            "context": meaning,
            "status":"generated"
        }


live_conversation_brain = LiveConversationBrain()
