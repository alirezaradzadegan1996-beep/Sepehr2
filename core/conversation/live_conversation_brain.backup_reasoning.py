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

        text = meaning.get("input","")

        memory_context = meaning.get("memory_context") or {}
        experiences = meaning.get("experiences") or []

        memories = experience_memory.recall()["experiences"]

        experience_count = memory_context.get(
            "memory_boost",
            {}
        ).get(
            "experience_count",
            len(experiences)
        )

        recommended = memory_context.get(
            "memory_boost",
            {}
        ).get(
            "recommended_capability"
        )


        # remember user name
        if "اسم من" in text and "است" in text:

            name = text.replace("اسم من","").replace("است","").strip()

            experience_memory.save({
                "type":"profile",
                "key":"name",
                "value":name,
                "goal":text,
                "skill":"conversation",
                "success":True
            })

            profile_memory.save("name", name)
            response = f"خوشبختم {name}، به خاطر سپردم."


        elif "اسم من چی بود" in text or "اسمم چی بود" in text:

            name = None

            for item in memories:
                name = profile_memory.get("name")

            if name:
                response = f"اسم شما {name} است."
            else:
                response = "هنوز اسم شما را نمی‌دانم."


        else:

            reasoning = reasoning_bridge.think(text)

            solution = reasoning.get(
                "solution"
            )

            if solution:

                response = solution

            elif experience_count > 0:

                response = (
                    f"من {experience_count} تجربه مشابه در حافظه دارم."
                )

            else:

                response = "سلام، در خدمتت هستم."


        return {
            "response": response,
            "context": meaning,
            "status": "generated"
        }


live_conversation_brain = LiveConversationBrain()
