import uuid

from core.identity.device.device_profile import device_profile


class DeviceActivation:


    def activate(self, device_id, owner):

        existing = device_profile.find_device(device_id)


        if existing:

            return {
                "status":"DEVICE_ALREADY_ACTIVE",
                "device":device_id
            }


        token = str(uuid.uuid4())


        result = device_profile.register_device(
            device_id,
            owner
        )


        return {
            "activation_token":token,
            "owner":owner,
            "result":result,
            "status":"DEVICE_ACTIVATED"
        }



device_activation = DeviceActivation()
