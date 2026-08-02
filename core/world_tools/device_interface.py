

class DeviceInterface:

    def connect(self,device):
        return {
            "device":device,
            "control":"available",
            "status":"DEVICE_CONTROL_INTERFACE_ACTIVE"
        }


device_interface=DeviceInterface()

