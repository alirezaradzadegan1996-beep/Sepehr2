from core.learning.priority_reasoner import priority_reasoner
from core.goals.learning_bridge import goal_learning_bridge
from core.learning.executor import learning_executor


class AutonomousGoalRunner:


    def run(self, goal):


        bridge = goal_learning_bridge.build(goal)


        ranked = priority_reasoner.rank(
            bridge["learning_tasks"]
        )


        if not ranked:

            return {
                "status":"completed"
            }


        next_task = ranked[0]


        result = learning_executor.execute(
            {
                "skill": next_task["skill"],
                "priority": next_task["priority"],
                "status":"waiting"
            }
        )


        return {

            "goal":goal,

            "selected":next_task,

            "execution":result

        }



autonomous_goal_runner = AutonomousGoalRunner()
