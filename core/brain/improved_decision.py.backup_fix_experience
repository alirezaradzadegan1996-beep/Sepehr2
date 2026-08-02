from core.memory.experience_analyzer import experience_analyzer
from core.learning.insight_engine import learning_insight


class ImprovedDecision:


    def decide(self, skill):


        experiences = experience_analyzer.analyze(
            skill
        )


        insights = learning_insight.generate()


        related = []


        for item in insights:

            if item.get("skill") == skill:

                related.append(
                    item
                )


        if related:


            return {

                "skill": skill,

                "experience_found": True,

                "past_insights": related,

                "decision":
                "use_previous_learning"

            }


        return {

            "skill": skill,

            "experience_found": False,

            "past_insights": [],

            "decision":
            "create_new_learning_path"

        }



improved_decision = ImprovedDecision()
