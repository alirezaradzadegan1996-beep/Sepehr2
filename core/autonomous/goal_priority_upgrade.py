
class GoalPriority:

    def select(self, goals):

        return {
            "selected": goals,
            "priority": "high",
            "status": "selected"
        }


goal_priority_upgrade = GoalPriority()
