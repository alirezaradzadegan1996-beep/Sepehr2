

class DeviceControl:

    def connect(self):
        return {
            "device":"connected",
            "status":"DEVICE_CONTROL_INTERFACE_ACTIVE"
        }


device_control=DeviceControl()

