
class SensorCore:

    def read(self, source):
        return {
            "source": source,
            "status": "received"
        }

sensor_core = SensorCore()
