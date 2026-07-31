class LongTermPlanner:


    def plan(self, goal):

        return {
            "goal":goal,
            "timeline":[
                "short_term",
                "medium_term",
                "long_term"
            ],
            "status":"planned"
        }


long_term_planner = LongTermPlanner()
