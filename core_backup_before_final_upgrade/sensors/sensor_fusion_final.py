from datetime import datetime


class VisionSensor:

    def observe(self):

        return {
            "source":"vision",
            "object":"unknown_object",
            "confidence":0.5
        }



class VoiceSensor:

    def observe(self):

        return {
            "source":"voice",
            "text":"unknown speech",
            "confidence":0.5
        }



class SensorFusion:

    def __init__(self):

        self.vision = VisionSensor()
        self.voice = VoiceSensor()


    def combine(self):

        observations = [
            self.vision.observe(),
            self.voice.observe()
        ]

        return {
            "time":str(datetime.now()),
            "sources":[
                "vision",
                "voice"
            ],
            "observations":observations,
            "interpretation":"environment understood",
            "status":"fused"
        }



fusion = SensorFusion()


print(
    fusion.combine()
)

