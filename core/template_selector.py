from core.experience_memory import ExperienceMemory


class TemplateSelector:

    def __init__(self):
        self.memory = ExperienceMemory()


    def select(self, project_type):

        experience = self.memory.get_best_practices(
            project_type
        )


        if not experience.get("found"):
            return "basic"


        confidence = experience.get(
            "confidence",
            "low"
        )


        if confidence in [
            "medium",
            "high"
        ]:
            return "advanced"


        return "basic"
