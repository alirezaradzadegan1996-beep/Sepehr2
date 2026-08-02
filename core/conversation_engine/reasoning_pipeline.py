

class ReasoningPipeline:

    def think(self,question):
        return {
            "reasoning":"completed",
            "status":"REASONING_RESPONSE_PIPELINE_ACTIVE"
        }


reasoning_pipeline=ReasoningPipeline()

