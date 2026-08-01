
from core.evolution.capability_performance import capability_performance


class SelfImprovementEngine:


    def analyze(self, name):

        data = capability_performance.get(name)

        if not data:

            return {
                "capability": name,
                "status": "unknown"
            }


        score = data.get(
            "score",
            0
        )


        if score >= 0.9:

            return {
                "capability": name,
                "status": "promoted",
                "action": "increase_priority",
                "score": score
            }


        if score < 0.5:

            return {
                "capability": name,
                "status": "needs_improvement",
                "action": "learn_more",
                "score": score
            }


        return {
            "capability": name,
            "status": "stable",
            "action": "monitor",
            "score": score
        }



self_improvement = SelfImprovementEngine()
