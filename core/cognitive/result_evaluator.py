
class ResultEvaluator:

    def evaluate(self,result):

        return {
            "result":result,
            "score":100,
            "status":"evaluated"
        }


result_evaluator = ResultEvaluator()
