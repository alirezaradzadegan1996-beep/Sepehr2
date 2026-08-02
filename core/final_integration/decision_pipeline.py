

class DecisionPipeline:


    def decide(self, analysis):

        return {

            "analysis":
                analysis,

            "decision":
                "selected",

            "status":
                "DECISION_PIPELINE_ACTIVE"

        }


decision_pipeline = DecisionPipeline()

