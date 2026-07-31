from core.learning.strategy_engine import learning_strategy
from core.learning.insight_engine import learning_insight


class SelfImprovementEngine:


    def analyze(self):

        strategy = learning_strategy.analyze()

        insights = learning_insight.generate()


        suggestions = []


        if strategy["failed"] > 0:

            suggestions.append(
                {
                    "area":"failure_handling",
                    "reason":"failed experiences detected",
                    "priority":8
                }
            )


        if strategy["successful"] > 0:

            suggestions.append(
                {
                    "area":"pattern_reuse",
                    "reason":"successful patterns available",
                    "priority":7
                }
            )


        return {

            "strategy":strategy,

            "insights":insights,

            "suggestions":suggestions

        }



self_improvement_engine = SelfImprovementEngine()
