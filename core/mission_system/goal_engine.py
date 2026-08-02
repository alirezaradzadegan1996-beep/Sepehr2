

class GoalEngine:

    def understand(self,goal):
        return {
            "goal":goal,
            "understood":True,
            "status":"GOAL_UNDERSTANDING_ENGINE_ACTIVE"
        }


goal_engine=GoalEngine()

