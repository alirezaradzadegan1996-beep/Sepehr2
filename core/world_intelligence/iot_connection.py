

class IoTConnection:

    def connect(self,node):
        return {
            "node":node,
            "iot":"connected",
            "status":"IOT_CONNECTION_CORE_ACTIVE"
        }


iot_connection=IoTConnection()

