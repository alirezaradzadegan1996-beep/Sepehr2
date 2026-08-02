

class DecisionLayer:

    def decide(self,input_data):
        return {
            "input":input_data,
            "decision":"generated",
            "status":"REAL_WORLD_DECISION_ACTIVE"
        }


decision_layer=DecisionLayer()

