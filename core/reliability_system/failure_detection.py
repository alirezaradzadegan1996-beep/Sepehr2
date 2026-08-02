

class FailureDetection:

    def detect(self,event):
        return {
            "event":event,
            "failure":"identified",
            "status":"FAILURE_DETECTION_ACTIVE"
        }


failure_detection=FailureDetection()

