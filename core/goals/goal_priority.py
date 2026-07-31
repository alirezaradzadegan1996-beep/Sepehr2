class GoalPriorityEngine:


    def select(self, goals):

        if not goals:

            return None


        selected = max(
            goals,
            key=lambda x: x.get("priority",0)
        )


        return {

            "selected": selected,

            "reason":"highest priority goal"

        }



goal_priority = GoalPriorityEngine()
