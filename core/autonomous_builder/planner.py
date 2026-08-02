

class BuilderPlanner:

    def create_plan(self,idea):

        return {

            "idea":idea,
            "plan":"generated",
            "status":"BUILDER_PLANNING_ACTIVE"

        }


planner=BuilderPlanner()

