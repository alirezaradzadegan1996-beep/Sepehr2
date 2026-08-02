

class MissionEvaluator:

    def evaluate(self,result):
        return {
            "result":result,
            "quality":"measured",
            "status":"MISSION_EVALUATION_ACTIVE"
        }


mission_evaluator=MissionEvaluator()

