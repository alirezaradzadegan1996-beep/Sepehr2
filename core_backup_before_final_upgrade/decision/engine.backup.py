from core.capabilities import registry


class DecisionEngine:


    def decide(self, text):

        results = []

        for name in registry.list():

            capability = registry.get(name)

            if hasattr(capability, "can_handle"):

                try:
                    if capability.can_handle(text):
                        results.append(name)

                except Exception:
                    pass


        if not results:
            return None


        return {
            "capability": results[0],
            "candidates": results
        }


decision_engine = DecisionEngine()
