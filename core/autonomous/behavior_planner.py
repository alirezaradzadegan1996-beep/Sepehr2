class BehaviorPlanner:


    def plan(self, goal):

        return {
            "goal":goal,
            "steps":[
                "analyze",
                "execute",
                "evaluate"
            ],
            "status":"planned"
        }


behavior_planner = BehaviorPlanner()
