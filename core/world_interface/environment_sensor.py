

class EnvironmentSensor:


    def scan(self):

        return {

            "environment":
                "detected",

            "signals":
                "collected",

            "status":
                "ENVIRONMENT_SENSOR_ACTIVE"

        }


environment_sensor = EnvironmentSensor()

