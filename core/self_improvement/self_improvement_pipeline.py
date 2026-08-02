from core.self_improvement.improvement_manager import self_improvement_manager
from core.self_improvement.improvement_memory import improvement_memory
from core.self_improvement.patch_generator import patch_generator
from core.self_improvement.improvement_tester import improvement_tester


class SelfImprovementPipeline:

    def run(self, task, experience, memory, decision):

        analysis = self_improvement_manager.analyze(
            task,
            experience,
            memory,
            decision
        )

        if analysis.get("status") != "improvement_needed":
            return {
                "status":"no_improvement_needed",
                "analysis":analysis
            }

        improvement_memory.save({
            "task":task,
            "analysis":analysis,
            "status":"detected"
        })

        plan = analysis.get("plan",{})

        patches = patch_generator.generate(
            plan
        )

        test = improvement_tester.test(
            patches
        )

        improvement_memory.save({
            "task":task,
            "patches":patches,
            "test":test,
            "status":"ready"
        })

        return {
            "status":"improvement_ready",
            "analysis":analysis,
            "patches":patches,
            "test":test
        }


self_improvement_pipeline = SelfImprovementPipeline()
