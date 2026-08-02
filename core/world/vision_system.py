
class VisionSystem:

    def analyze(self, image):
        return {
            "image": image,
            "objects": [],
            "status": "analyzed"
        }

vision_system = VisionSystem()
