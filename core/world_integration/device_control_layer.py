

class DeviceControlLayer:


    def control(self, device):

        return {

            "device":
                device,

            "connection":
                "active",

            "action":
                "executed",

            "status":
                "DEVICE_CONTROL_ACTIVE"

        }



device_control_layer = DeviceControlLayer()

