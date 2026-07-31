from core.memory.improvement_memory import improvement_memory


class ImprovementEvaluator:


    def evaluate(self):

        records = improvement_memory.recall()


        evaluations = []


        for item in records:


            action = item.get("action")


            score = 0

            impact = "unknown"


            if "upgrade" in action:

                score = 8

                impact = "positive"


            elif "analysis" in action:

                score = 6

                impact = "informational"


            evaluations.append(
                {
                    "action": action,
                    "impact": impact,
                    "score": score
                }
            )


        return evaluations



improvement_evaluator = ImprovementEvaluator()
