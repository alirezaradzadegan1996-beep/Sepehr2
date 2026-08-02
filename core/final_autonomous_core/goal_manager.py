

class GoalManager:

    def manage(self,goal):
        return {
            "goal":goal,
            "planning":"completed",
            "status":"AUTONOMOUS_GOAL_MANAGER_ACTIVE"
        }


goal_manager=GoalManager()

