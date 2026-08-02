
class DecisionEvolutionRouter:


    def decide(self, situation):

        if situation.get("missing_capability"):

            return {

                "decision":
                    "evolve",

                "target":
                    situation["missing_capability"],

                "status":
                    "EVOLUTION_REQUIRED"

            }


        return {

            "decision":
                "normal_execution",

            "status":
                "NO_EVOLUTION_REQUIRED"

        }



decision_evolution_router = DecisionEvolutionRouter()

