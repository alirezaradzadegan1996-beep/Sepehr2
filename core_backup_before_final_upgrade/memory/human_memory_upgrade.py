from datetime import datetime


class HumanMemory:

    def __init__(self):

        self.short_term = []
        self.long_term = []
        self.experiences = []


    def remember(self, event, important=False):

        memory = {
            "event": event,
            "time": str(datetime.now())
        }

        self.short_term.append(memory)

        if important:
            self.long_term.append(memory)

        return {
            "stored": True,
            "important": important,
            "short_term": len(self.short_term),
            "long_term": len(self.long_term)
        }


    def learn_from_experience(self, experience):

        self.experiences.append(experience)

        return {
            "experience_saved": True,
            "count": len(self.experiences)
        }



memory = HumanMemory()


print(
    memory.remember(
        "completed voice and face integration",
        True
    )
)


print(
    memory.learn_from_experience(
        "owner interaction pattern"
    )
)


print(
    {
        "status":"human_memory_upgrade_active",
        "time":str(datetime.now())
    }
)

