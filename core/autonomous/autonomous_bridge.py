
from core.autonomous.goal_manager import goal_manager
from core.autonomous.decision_loop import decision_loop
from core.autonomous.action_selector import action_selector
from core.autonomous.scheduler import scheduler
from core.autonomous.adaptive_learning import adaptive_learning
from core.autonomous.experience_analyzer import experience_analyzer
from core.autonomous.strategy_optimizer import strategy_optimizer


class AutonomousBridge:

    def run(self, goal):

        created = goal_manager.create_goal(goal)

        decision = decision_loop.decide(
            created
        )

        action = action_selector.select(
            ["learn","execute"]
        )

        task = scheduler.schedule(
            action
        )

        experience = experience_analyzer.analyze(
            task
        )

        learning = adaptive_learning.learn(
            experience
        )

        strategy = strategy_optimizer.optimize(
            learning
        )

        return {
            "goal":created,
            "decision":decision,
            "action":action,
            "task":task,
            "experience":experience,
            "learning":learning,
            "strategy":strategy
        }


autonomous_bridge=AutonomousBridge()
