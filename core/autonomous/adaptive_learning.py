class AdaptiveLearning:


    def __init__(self):
        self.lessons=[]


    def learn(self, experience):

        self.lessons.append(
            experience
        )

        return {
            "status":"learned",
            "lessons":len(self.lessons)
        }


adaptive_learning = AdaptiveLearning()
