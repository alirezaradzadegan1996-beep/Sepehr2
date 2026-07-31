from core.goals.decision import goal_decision
from core.learning.priority_engine import learning_priority


class GoalLearningBridge:


    def build(self, goal):


        decision = goal_decision.decide(goal)


        tasks = []


        for item in decision["missing"]:

            skill = item["need"]


            priority = 8


            task = learning_priority.add(
                {
                    "task": skill,
                    "importance": priority
                }
            )


            tasks.append(task)



        return {

            "goal": goal,

            "learning_tasks": tasks

        }



goal_learning_bridge = GoalLearningBridge()
