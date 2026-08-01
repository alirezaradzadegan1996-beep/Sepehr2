from core.memory.experience_memory import experience_memory


class LearningInsightEngine:


    def generate(self):

        experiences = experience_memory.recall()

        insights = []


        for item in experiences:


            skill = (
                item.get("skill")
                or
                item.get("input")
                or
                item.get("event")
                or
                "unknown"
            )


            result = item.get("result")


            if result == "success":

                insights.append({

                    "skill": skill,

                    "type":"success_pattern",

                    "insight":
                    item.get("lesson","success learned")

                })


            elif item.get("evaluation"):


                insights.append({

                    "skill": skill,

                    "type":"failure_pattern",

                    "insight":
                    "missing capability detected"

                })


            else:

                insights.append({

                    "skill": skill,

                    "type":"experience",

                    "insight":
                    item.get("text","general experience")

                })


        return insights



learning_insight = LearningInsightEngine()
