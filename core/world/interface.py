class WorldInterface:


    def __init__(self):

        self.sensors = {}



    def register(self, name, sensor):

        self.sensors[name] = sensor


        return {
            "sensor": name,
            "status": "registered"
        }



    def observe(self):

        result = {}


        for name, sensor in self.sensors.items():

            try:

                result[name] = sensor.read()

            except Exception as e:

                result[name] = {
                    "error": str(e)
                }


        return result



world_interface = WorldInterface()
