

class GoalEngine:

    def understand(self,goal):
        return {
            "goal":goal,
            "analysis":"completed",
            "status":"GOAL_UNDERSTANDING_ACTIVE"
        }


goal_engine=GoalEngine()

