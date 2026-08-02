
class SelfEvaluation:

    def evaluate(self, result):

        return {
            "result": result,
            "score": 100,
            "feedback": "generated",
            "status": "SELF_EVALUATION_ACTIVE"
        }


self_evaluation = SelfEvaluation()
