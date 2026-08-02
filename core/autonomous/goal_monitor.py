
class GoalMonitor:

    def check(self, result):

        return {
            "result":result,
            "progress":100,
            "status":"completed"
        }


goal_monitor = GoalMonitor()
