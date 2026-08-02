
from core.vision.image_input import image_input
from core.vision.object_detector import object_detector
from core.vision.scene_analyzer import scene_analyzer


class VisionRuntime:

    def process(self, image):

        received = image_input.receive(
            image
        )

        objects = object_detector.detect(
            received
        )

        scene = scene_analyzer.analyze(
            objects
        )

        return {
            "input": received,
            "objects": objects,
            "scene": scene,
            "status": "VISION_ACTIVE"
        }


vision_runtime = VisionRuntime()
