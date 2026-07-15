from core.experience_memory import ExperienceMemory


class ExperienceBridge:

    def __init__(self):
        self.memory = ExperienceMemory()


    def enrich_reasoning(self, project_type, reasoning):

        experience = self.memory.get_best_practices(
            project_type
        )


        if not experience.get("found"):

            reasoning["experience_memory_used"] = False
            return reasoning



        reasoning["experience_memory"] = experience


        confidence = experience.get(
            "confidence",
            "low"
        )


        reasoning["experience_confidence"] = confidence


        learned_files = experience.get(
            "files",
            []
        )


        learned_features = experience.get(
            "features",
            []
        )


        learned_suggestions = experience.get(
            "suggestions",
            []
        )


        # همیشه ویژگی‌های یادگرفته شده را اضافه کن
        reasoning["suggestions"] = list(
            dict.fromkeys(
                reasoning.get("suggestions", [])
                +
                learned_features
                +
                learned_suggestions
            )
        )


        # اعتماد متوسط و بالا اجازه افزودن فایل می‌دهد
        if confidence in [
            "medium",
            "high"
        ]:

            reasoning["modules"] = list(
                dict.fromkeys(
                    reasoning.get("modules", [])
                    +
                    learned_files
                )
            )


        reasoning["learned_files"] = learned_files

        reasoning["learned_features"] = learned_features


        reasoning["experience_memory_used"] = True


        reasoning["experience_source"] = (
            "ExperienceMemory"
        )


        return reasoning
