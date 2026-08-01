from core.learning.insight_engine import learning_insight
from core.memory.improvement_memory import improvement_memory


class ImprovementActionEngine:


    def execute(self, task):

        insights = learning_insight.generate()


        result = None


        if task["task"] == "upgrade_failure_system":

            failures = [
                i for i in insights
                if i.get("type") == "failure_pattern"
            ]


            result = {

                "action":"failure_analysis",

                "status":"completed",

                "found_failures":len(failures),

                "data":failures

            }



        elif task["task"] == "upgrade_pattern_system":

            patterns = [
                i for i in insights
                if i.get("type") == "success_pattern"
            ]


            result = {

                "action":"pattern_extraction",

                "status":"completed",

                "found_patterns":len(patterns),

                "data":patterns

            }



        else:

            result = {

                "status":"unknown_improvement"

            }



        # ذخیره نتیجه بهبود

        improvement_memory.add(
            task["task"],
            result
        )


        return result



improvement_action = ImprovementActionEngine()
