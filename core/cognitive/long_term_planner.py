
class LongTermPlanner:

    def plan(self, goal):

        return {
            "goal": goal,
            "steps": [
                "analyze",
                "learn",
                "execute"
            ],
            "status": "planned"
        }


long_term_planner = LongTermPlanner()
