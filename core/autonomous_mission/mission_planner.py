

class MissionPlanner:

    def plan(self,goal):
        return {
            "goal":goal,
            "plan":"generated",
            "status":"MISSION_PLANNING_ACTIVE"
        }


mission_planner=MissionPlanner()

