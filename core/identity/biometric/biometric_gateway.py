import json
from pathlib import Path


class BiometricGateway:


    def __init__(self):

        self.file = Path("data/biometric_profile.json")
        self.profile = {}

        self.load()


    def load(self):

        if self.file.exists():

            try:
                self.profile = json.loads(
                    self.file.read_text(
                        encoding="utf-8"
                    )
                )

            except Exception:
                self.profile = {}


    def register_biometric(self, owner):

        self.profile = {
            "owner": owner,
            "biometric_enabled": True,
            "method": "android_system_biometric"
        }


        self.file.write_text(
            json.dumps(
                self.profile,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )


        return {
            "status":"BIOMETRIC_REGISTERED",
            "owner":owner
        }


    def verify(self, result):

        if (
            self.profile.get("biometric_enabled")
            and result is True
        ):

            return {
                "access":True,
                "level":"OWNER",
                "status":"BIOMETRIC_VERIFIED"
            }


        return {
            "access":False,
            "level":"UNKNOWN",
            "status":"BIOMETRIC_FAILED"
        }



biometric_gateway = BiometricGateway()
