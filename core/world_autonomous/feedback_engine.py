

class FeedbackEngine:

    def process(self,result):
        return {
            "result":result,
            "feedback":"processed",
            "status":"FEEDBACK_PROCESSING_ACTIVE"
        }


feedback_engine=FeedbackEngine()

