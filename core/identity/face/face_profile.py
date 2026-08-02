import json
from pathlib import Path


class FaceProfile:


    def __init__(self):

        self.file = Path("data/face_profile.json")
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


    def register_face(self, owner, signature):

        self.profile = {
            "owner": owner,
            "signature": signature,
            "registered": True
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
            "status": "FACE_REGISTERED",
            "owner": owner
        }


    def get_face(self):

        return self.profile



face_profile = FaceProfile()
