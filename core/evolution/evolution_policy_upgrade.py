
class EvolutionPolicy:

    def decide(self, analysis):

        return {
            "analysis": analysis,
            "policy": "upgrade",
            "status": "selected"
        }


evolution_policy_upgrade = EvolutionPolicy()
