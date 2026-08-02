
class GoalManager:

    def create(self, goal):

        return {
            "goal": goal,
            "priority": "high",
            "tracking": "enabled",
            "status": "GOAL_MANAGER_ACTIVE"
        }


goal_manager = GoalManager()
