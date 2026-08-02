

class EnvironmentLearning:

    def learn(self,result):
        return {
            "experience":result,
            "learning":"updated",
            "status":"ENVIRONMENT_LEARNING_CORE_ACTIVE"
        }


environment_learning=EnvironmentLearning()

