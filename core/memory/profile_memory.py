import json
from pathlib import Path


class ProfileMemory:

    def __init__(self):
        self.file = Path("data/profile_memory.json")

        if not self.file.exists():
            self.file.write_text(
                "{}",
                encoding="utf-8"
            )


    def load(self):
        try:
            return json.loads(
                self.file.read_text(
                    encoding="utf-8"
                )
            )
        except:
            return {}


    def save(self,key,value):

        data = self.load()

        data[key] = value

        self.file.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

        return data


    def get(self,key):

        return self.load().get(key)


profile_memory = ProfileMemory()
