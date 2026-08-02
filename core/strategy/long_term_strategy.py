
class LongTermStrategy:

    def create(self, objective):

        return {
            "objective": objective,
            "timeline": "long_term",
            "strategy": "generated",
            "status": "LONG_TERM_STRATEGY_ACTIVE"
        }


long_term_strategy = LongTermStrategy()
