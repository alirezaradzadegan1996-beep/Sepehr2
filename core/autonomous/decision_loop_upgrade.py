
class DecisionLoop:

    def decide(self, goal):

        return {
            "goal": goal,
            "decision": "continue",
            "status": "decided"
        }


decision_loop_upgrade = DecisionLoop()
