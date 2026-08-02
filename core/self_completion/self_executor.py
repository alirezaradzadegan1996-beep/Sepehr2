from core.self_completion.self_planner import self_planner


class SelfExecutor:


    def execute(self):

        plan = self_planner.create_plan()

        results=[]


        for task in plan:

            results.append(
                {
                    "task":task,
                    "status":"ready_for_builder"
                }
            )


        return results



self_executor = SelfExecutor()
