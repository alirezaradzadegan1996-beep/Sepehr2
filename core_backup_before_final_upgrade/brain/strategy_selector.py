from core.memory.strategy_memory import strategy_memory


class StrategySelector:


    def select(self, action):

        strategies = strategy_memory.recall()


        matches = [
            x for x in strategies
            if x.get("action") == action
        ]


        if matches:

            best = max(
                matches,
                key=lambda x: x.get("confidence",0)
            )

            return {
                "action": action,
                "strategy_found": True,
                "selected": best,
                "decision":"reuse_strategy"
            }


        return {
            "action": action,
            "strategy_found": False,
            "decision":"create_new_strategy"
        }



strategy_selector = StrategySelector()
