from core.experience_memory import ExperienceMemory
from core.repair_memory import RepairMemory


class ProjectLearningEngine:

    def __init__(self):

        self.experience = ExperienceMemory()
        self.repair = RepairMemory()


    def learn_context(self, project_type):

        result = {
            "project_type": project_type,
            "experience": None,
            "repairs": [],
            "suggestions": []
        }


        # تجربه پروژه‌های موفق
        experience = self.experience.get_best_practices(
            project_type
        )


        if experience.get("found"):

            result["experience"] = experience

            result["suggestions"].extend(
                experience.get(
                    "features",
                    []
                )
            )


        # خطاهای قبلی
        try:

            repairs = self.repair.get_solutions(
                project_type
            )

            if repairs:

                result["repairs"] = repairs

                for item in repairs:

                    if item.get("solution"):

                        result["suggestions"].append(
                            item["solution"]
                        )

        except Exception:

            pass


        result["suggestions"] = list(
            set(
                result["suggestions"]
            )
        )


        return result



    def improve_analysis(self, analysis):

        project_type = analysis.get(
            "type",
            "general"
        )


        learning = self.learn_context(
            project_type
        )


        analysis["learning"] = learning


        if learning.get("suggestions"):

            features = analysis.get(
                "features",
                []
            )


            for item in learning["suggestions"]:

                if item not in features:

                    features.append(item)


            analysis["features"] = features


        return analysis
