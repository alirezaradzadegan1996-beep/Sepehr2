from core.brain.improvement_evaluator import improvement_evaluator


class StrategyFeedback:


    def analyze(self):

        evaluations = improvement_evaluator.evaluate()

        feedback = []


        for item in evaluations:

            if item["score"] >= 8:

                feedback.append(
                    {
                        "action": item["action"],
                        "status":"preferred",
                        "confidence":0.8
                    }
                )


            elif item["score"] < 5:

                feedback.append(
                    {
                        "action": item["action"],
                        "status":"avoid",
                        "confidence":0.3
                    }
                )


        return feedback



strategy_feedback = StrategyFeedback()
