from core.brain.self_improvement_engine import self_improvement_engine


class ImprovementPlanner:


    def plan(self):

        analysis = self_improvement_engine.analyze()

        plans = []


        for item in analysis["suggestions"]:

            if item["area"] == "failure_handling":

                plans.append(
                    {
                        "task":"upgrade_failure_system",
                        "action":"improve error learning",
                        "priority":item["priority"]
                    }
                )


            elif item["area"] == "pattern_reuse":

                plans.append(
                    {
                        "task":"upgrade_pattern_system",
                        "action":"reuse successful experiences",
                        "priority":item["priority"]
                    }
                )


        return plans



improvement_planner = ImprovementPlanner()
