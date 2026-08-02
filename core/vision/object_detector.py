
class ObjectDetector:

    def detect(self, image):

        return {
            "image": image,
            "objects": [
                "unknown_object"
            ],
            "status": "detected"
        }


object_detector = ObjectDetector()
