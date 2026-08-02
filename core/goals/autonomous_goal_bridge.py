
from core.goals.autonomous_goal_generator import autonomous_goal_generator
from core.goals.goal_prioritizer import goal_prioritizer
from core.goals.action_planner import action_planner


class AutonomousGoalBridge:

    def run(self, context):

        goal = autonomous_goal_generator.create(context)

        priority = goal_prioritizer.prioritize(goal)

        plan = action_planner.plan(priority)

        return {
            "goal":goal,
            "priority":priority,
            "plan":plan,
            "status":"ready"
        }


autonomous_goal_bridge = AutonomousGoalBridge()
