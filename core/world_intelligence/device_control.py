

class DeviceControl:

    def connect(self,device):
        return {
            "device":device,
            "connection":"active",
            "status":"DEVICE_CONTROL_LAYER_ACTIVE"
        }


device_control=DeviceControl()

