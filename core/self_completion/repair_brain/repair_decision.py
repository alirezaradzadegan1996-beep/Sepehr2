from core.self_completion.repair_memory.repair_memory import repair_memory


class RepairDecision:

    def decide(self, problem):

        memories = repair_memory.search(problem)

        if memories:

            return {
                "decision":"use_previous_solution",
                "problem":problem,
                "memory":memories[0],
                "confidence":1.0
            }


        return {
            "decision":"create_new_solution",
            "problem":problem,
            "confidence":0.5
        }


repair_decision = RepairDecision()
