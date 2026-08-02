from core.self_completion.project_analyzer import project_analyzer
from core.self_completion.gap_detector import gap_detector
from core.self_completion.improvement_queue import improvement_queue
from core.self_completion.improvement_planner import improvement_planner
from core.self_completion.priority_selector import priority_selector
from core.self_completion.evolution_memory.evolution_memory import evolution_memory
from core.self_completion.executor.self_executor_engine import self_executor_engine


class SelfCompletionEngine:

    def run_analysis(self):

        analysis = project_analyzer.analyze()

        gaps = gap_detector.detect()

        # فقط Gapهای جدید را وارد صف کن
        if gaps.get("count",0):
            improvement_queue.build(gaps)

        # صف واقعی
        queue = improvement_queue.get()

        plan = improvement_planner.create_plan(
            [i["target"] for i in queue if i["type"]=="missing_module"]
        )

        priority = priority_selector.select(plan)

        executed=[]

        for task in priority:
            try:
                executed.append(
                    self_executor_engine.execute(task)
                )
            except Exception as e:
                executed.append({
                    "target":task.get("target"),
                    "status":"failed",
                    "error":str(e)
                })

        for item in executed:
            evolution_memory.save({
                "type": "self_completion",
                "target": item.get("target"),
                "status": item.get("status"),
                "result": "success"
            })

        return {
            "analysis":analysis,
            "gaps":gaps,
            "queue":queue,
            "plan":plan,
            "priority_plan":priority,
            "executed":executed
        }


self_completion_engine=SelfCompletionEngine()
