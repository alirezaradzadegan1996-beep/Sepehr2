from collections import defaultdict


class ExperienceAnalyzer:

    def analyze(self, task, experiences):

        similar = []

        words = set(task.split())

        for exp in experiences:

            text = str(
                exp.get("goal")
                or exp.get("input")
                or ""
            )

            score = len(
                words.intersection(
                    set(text.split())
                )
            )

            if score > 0:
                similar.append(
                    {
                        "experience": exp,
                        "score": score
                    }
                )

        similar.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        success = [
            x for x in similar
            if x["experience"].get("result") == "success"
        ]

        return {
            "task": task,
            "similar_count": len(similar),
            "successful_count": len(success),
            "best": (
                success[0]
                if success
                else None
            ),
            "confidence": (
                min(len(success) / 5, 1)
            )
        }


experience_analyzer = ExperienceAnalyzer()
