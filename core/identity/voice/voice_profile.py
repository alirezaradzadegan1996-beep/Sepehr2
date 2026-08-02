import json
from pathlib import Path


class VoiceProfile:


    def __init__(self):

        self.file = Path("data/voice_profile.json")
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


    def register_voice(self, owner, signature):

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
            "status": "VOICE_REGISTERED",
            "owner": owner
        }


    def get_voice(self):

        return self.profile



voice_profile = VoiceProfile()
