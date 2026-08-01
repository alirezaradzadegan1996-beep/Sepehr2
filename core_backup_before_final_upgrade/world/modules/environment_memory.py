class EnvironmentMemory:

    def __init__(self):
        self.history=[]


    def remember(self, context):

        self.history.append(context)

        return {
            "status":"stored",
            "count":len(self.history)
        }


    def recall(self):
        return self.history



environment_memory = EnvironmentMemory()
