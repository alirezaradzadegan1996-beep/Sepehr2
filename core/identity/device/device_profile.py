import json
from pathlib import Path


class DeviceProfile:


    def __init__(self):

        self.file = Path("data/device_profile.json")
        self.devices = []

        self.load()


    def load(self):

        if self.file.exists():

            try:
                self.devices = json.loads(
                    self.file.read_text(
                        encoding="utf-8"
                    )
                )

            except Exception:
                self.devices = []


    def register_device(self, device_id, owner):

        device = {
            "device_id": device_id,
            "owner": owner,
            "active": True
        }


        self.devices.append(device)


        self.file.write_text(
            json.dumps(
                self.devices,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )


        return {
            "status":"DEVICE_REGISTERED",
            "device":device_id
        }


    def find_device(self, device_id):

        for device in self.devices:

            if device["device_id"] == device_id:
                return device


        return None



device_profile = DeviceProfile()
