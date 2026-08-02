from core.self_completion.improvement_queue import improvement_queue


class SelfPlanner:


    def create_plan(self):

        queue = improvement_queue.get()

        plan = []


        for item in queue:

            if item["type"] == "missing_module":

                plan.append(
                    {
                        "action":"create_module",
                        "target":item["target"],
                        "priority":item["priority"]
                    }
                )


        return plan



self_planner = SelfPlanner()
