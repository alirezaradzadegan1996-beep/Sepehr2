from collections import defaultdict


class FeedbackAnalyzer:

    def __init__(self):
        self.stats = defaultdict(
            lambda: {
                "success":0,
                "failed":0
            }
        )


    def analyze(self, experiences):

        for exp in experiences:

            skill = exp.get("skill")

            if not skill:
                continue

            if exp.get("result") == "success":
                self.stats[skill]["success"] += 1

            else:
                self.stats[skill]["failed"] += 1


        result = []

        for skill,data in self.stats.items():

            total = (
                data["success"]
                +
                data["failed"]
            )

            score = (
                data["success"] / total
                if total
                else 0
            )

            result.append(
                {
                    "capability":skill,
                    "success":data["success"],
                    "failed":data["failed"],
                    "score":score
                }
            )


        return sorted(
            result,
            key=lambda x:x["score"],
            reverse=True
        )


feedback_analyzer = FeedbackAnalyzer()
