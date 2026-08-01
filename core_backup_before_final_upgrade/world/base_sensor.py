class BaseSensor:


    name = "unknown"


    def read(self):

        return {
            "sensor": self.name,
            "status": "active"
        }
