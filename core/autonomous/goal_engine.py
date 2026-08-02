
class GoalEngine:

    def create(self, goal):

        return {
            "goal": goal,
            "status": "created"
        }


goal_engine = GoalEngine()
