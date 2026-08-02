

class ActionPlanner:

    def plan(self,goal):
        return {
            "goal":goal,
            "action":"planned",
            "status":"AUTONOMOUS_ACTION_PLANNER_ACTIVE"
        }


action_planner=ActionPlanner()

