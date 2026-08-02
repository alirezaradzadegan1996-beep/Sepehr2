
class ActionPlanner:

    def plan(self, goal):

        return {
            "goal": goal,
            "actions": [
                "analyze",
                "execute",
                "evaluate"
            ],
            "status": "planned"
        }


action_planner = ActionPlanner()
