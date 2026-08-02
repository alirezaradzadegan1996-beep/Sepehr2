

class SensorCore:

    def read(self):
        return {
            "sensor":"active",
            "data":"processed",
            "status":"SENSOR_INTEGRATION_CORE_ACTIVE"
        }


sensor_core=SensorCore()

