from core.capabilities.registry import registry
from core.evolution.evolution_memory import evolution_memory
from core.evolution.capability_state import capability_state


class EvolutionExecutor:

    def execute(self, decision):

        name = decision.get("capability")
        action = decision.get("action")

        cap = registry.find(name)

        if not cap:
            return {
                "status": "failed",
                "reason": "capability_not_found"
            }

        if action == "increase_priority":

            result = cap.improve()

            capability_state.update(
                name,
                {
                    "version": result.get("version"),
                    "status": "evolved"
                }
            )

            record = evolution_memory.record(
                {
                    "capability": name,
                    "action": action,
                    "version": result.get("version")
                }
            )

            return {
                "status": "evolved",
                "capability": name,
                "action": action,
                "result": result,
                "history": record
            }

        if action == "learn_more":
            return {
                "status": "learning_required",
                "capability": name
            }

        return {
            "status": "no_action",
            "capability": name
        }


evolution_executor = EvolutionExecutor()
