
from core.evolution.capability_performance import capability_performance

class EvolutionPolicy:

    MIN_USES = 5
    MIN_SCORE = 0.90

    def should_evolve(self, capability):

        stat = capability_performance.get(capability)

        if not stat:
            return False

        if stat.get("uses",0) < self.MIN_USES:
            return False

        if stat.get("score",0) < self.MIN_SCORE:
            return False

        return True


evolution_policy = EvolutionPolicy()
