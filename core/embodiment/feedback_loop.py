class FeedbackLoop:


    def __init__(self):
        self.history=[]


    def record(self, result):

        self.history.append(result)

        return {
            "status":"recorded",
            "count":len(self.history)
        }


    def recall(self):
        return self.history



feedback_loop = FeedbackLoop()
