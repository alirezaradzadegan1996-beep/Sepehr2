from core.world.base_sensor import BaseSensor


class CameraSensor(BaseSensor):


    name = "camera"


    def __init__(self):

        self.frames = 0



    def read(self):

        self.frames += 1


        return {

            "sensor":"camera",

            "status":"active",

            "frame_id":self.frames,

            "image":"simulated_frame"

        }



camera_sensor = CameraSensor()
