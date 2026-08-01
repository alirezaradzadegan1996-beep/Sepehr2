from collections import defaultdict


class MemoryIntelligence:


    def __init__(self):

        self.patterns = defaultdict(int)




    def analyze(self, experience):

        task = (
            experience.get("task")
            or experience.get("input")
            or experience.get("current_task")
            or experience.get("goal")
            or "unknown"
        )

        success = experience.get("success", False)

        self.patterns[task] += 1

        importance = 1

        if not success:
            importance += 5

        if self.patterns[task] > 3:
            importance += 3


        similar = []

        experiences = experience.get("experiences", [])

        for item in experiences:

            goal = str(
                item.get("goal","")
            )

            if goal and any(
                word in goal
                for word in task.split()
            ):

                similar.append(item)


        recommended_capability = None

        if similar:

            recommended_capability = similar[-1].get(
                "skill"
            )


        return {

            "task": task,

            "frequency": self.patterns[task],

            "importance": importance,

            "learning_needed": not success,

            "memory_boost": {

                "used": bool(similar),

                "experience_count": len(similar),

                "recommended_capability":
                    recommended_capability,

                "confidence":
                    min(
                        1.0,
                        len(similar) / 5
                    )
            }
        }


    def get_priorities(self):

        result = []


        for task,count in self.patterns.items():

            result.append({

                "task": task,

                "frequency": count

            })


        return result



memory_intelligence = MemoryIntelligence()
