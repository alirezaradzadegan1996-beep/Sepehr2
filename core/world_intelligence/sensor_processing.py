

class SensorProcessing:

    def read(self,sensor):
        return {
            "sensor":sensor,
            "data":"processed",
            "status":"SENSOR_PROCESSING_ENGINE_ACTIVE"
        }


sensor_processing=SensorProcessing()

