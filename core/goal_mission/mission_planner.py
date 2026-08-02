

class MissionPlanner:


    def plan(self, goal):

        return {

            "goal":
                goal,

            "steps":
                "generated",

            "strategy":
                "created",

            "status":
                "MISSION_PLANNING_ACTIVE"

        }



mission_planner = MissionPlanner()

