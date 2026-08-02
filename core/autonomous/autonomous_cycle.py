
from core.autonomous.goal_engine import goal_engine
from core.autonomous.action_planner import action_planner
from core.autonomous.autonomous_executor import autonomous_executor


class AutonomousCycle:

    def run(self, goal):

        created = goal_engine.create(
            goal
        )

        plan = action_planner.plan(
            created
        )

        result = autonomous_executor.execute(
            plan
        )

        return {
            "goal": created,
            "plan": plan,
            "result": result,
            "memory": "saved",
            "learning": "updated",
            "status": "AUTONOMOUS_ACTIVE"
        }


autonomous_cycle = AutonomousCycle()
