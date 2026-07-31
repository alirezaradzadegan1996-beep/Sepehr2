from core.brain.self_awareness import self_awareness
from core.learning.priority_engine import learning_priority


class SelfImprovement:


    def analyze(self):

        status = self_awareness.status()

        abilities = status["abilities"]


        suggestions = []


        if "vision" in abilities and "camera" not in abilities:

            suggestions.append(
                {
                    "skill":"camera",
                    "reason":"vision needs camera interface"
                }
            )


        return suggestions



    def learn_needed(self):

        suggestions = self.analyze()


        for item in suggestions:

            learning_priority.add(
                {
                    "task": item["skill"],
                    "importance": 7
                }
            )


        return suggestions



self_improvement = SelfImprovement()
