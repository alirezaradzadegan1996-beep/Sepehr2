
class WorldSensorBridge:

    def receive(self, source):

        return {
            "source": source,
            "status": "received"
        }


world_sensor_bridge = WorldSensorBridge()
