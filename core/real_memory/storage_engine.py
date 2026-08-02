

import json
from pathlib import Path


class MemoryStorage:

    def __init__(self):
        self.path = Path("data/real_memory.json")
        self.path.parent.mkdir(exist_ok=True)

        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")


    def save(self, memory):

        data=json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        data.append(memory)

        self.path.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

        return {
            "saved":True,
            "status":
            "MEMORY_STORAGE_ACTIVE"
        }



memory_storage = MemoryStorage()

