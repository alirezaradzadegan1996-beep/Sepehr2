from core.capabilities import registry


class DecisionEngine:


    def decide(self, text):

        scores = []


        for name in registry.list():

            capability = registry.get(name)

            score = 0


            if hasattr(capability, "score"):

                try:
                    score = capability.score(text)

                except Exception:
                    score = 0


            elif hasattr(capability, "can_handle"):

                try:
                    if capability.can_handle(text):
                        score = 1

                except Exception:
                    score = 0


            if score > 0:
                scores.append(
                    {
                        "capability": name,
                        "score": score
                    }
                )


        if not scores:
            return None


        scores.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return scores[0]


decision_engine = DecisionEngine()
