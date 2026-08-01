
class CapabilityMatcher:

    def score(self, text, capability):

        text = text.lower()

        score = 0

        name = getattr(capability, "name", "").lower()

        if name and name in text:
            score += 100

        purpose = getattr(capability, "purpose", "").lower()

        for word in purpose.split():
            if word in text:
                score += 10

        keywords = getattr(capability, "keywords", [])

        for key in keywords:
            if key.lower() in text:
                score += 20

        return score


    def match(self, text, registry):

        best = None
        best_score = 0

        for name, cap in registry.capabilities.items():

            s = self.score(text, cap)

            if s > best_score:
                best_score = s
                best = {
                    "name": name,
                    "capability": cap,
                    "score": s
                }

        return best
