class AutonomousDecisionLoop:


    def run(self, observation):

        return {
            "observation":observation,
            "decision":"continue",
            "status":"decided"
        }


decision_loop = AutonomousDecisionLoop()
