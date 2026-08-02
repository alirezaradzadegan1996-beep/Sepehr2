from datetime import datetime


class ImprovementPlanner:

    def create_plan(self, gaps):

        plan = []

        for gap in gaps:

            plan.append(
                {
                    "target": gap,
                    "actions": [
                        "analyze_requirement",
                        "generate_design",
                        "create_module",
                        "test_module",
                        "register_module"
                    ],
                    "priority": "high",
                    "created": str(datetime.now())
                }
            )

        return plan


improvement_planner = ImprovementPlanner()
