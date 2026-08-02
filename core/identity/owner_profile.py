import json
from pathlib import Path


class OwnerProfile:


    def __init__(self):

        self.file = Path("data/owner_profile.json")
        self.owner = {}

        self.load()


    def load(self):

        if self.file.exists():

            try:
                self.owner = json.loads(
                    self.file.read_text(
                        encoding="utf-8"
                    )
                )

            except Exception:
                self.owner = {}


    def register_owner(self, name):

        self.owner = {
            "name": name,
            "voice_registered": False,
            "face_registered": False,
            "device_verified": False
        }


        self.file.write_text(
            json.dumps(
                self.owner,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )


        return {
            "status": "OWNER_REGISTERED",
            "owner": name
        }


    def get_owner(self):

        return self.owner



owner_profile = OwnerProfile()
