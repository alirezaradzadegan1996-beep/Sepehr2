

class MemoryPrediction:

    def predict(self,data):
        return {
            "data":data,
            "prediction":"generated",
            "status":"MEMORY_PREDICTION_ACTIVE"
        }


memory_prediction=MemoryPrediction()

