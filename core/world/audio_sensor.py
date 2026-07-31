from core.world.base_sensor import BaseSensor


class AudioSensor(BaseSensor):


    name = "audio"


    def __init__(self):

        self.samples = 0



    def read(self):

        self.samples += 1


        return {

            "sensor":"audio",

            "status":"active",

            "sample_id":self.samples,

            "audio":"simulated_voice"

        }



audio_sensor = AudioSensor()
