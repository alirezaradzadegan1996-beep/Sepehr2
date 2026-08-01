import json
from pathlib import Path
from datetime import datetime


class CapabilityMemory:

    def __init__(self):
        self.path = Path("data/capability_memory.json")

        if not self.path.exists():
            self.path.write_text(
                "{}",
                encoding="utf-8"
            )


    def record(self,name,success=True):

        data=json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        if name not in data:
            data[name]={
                "version":1,
                "uses":0,
                "success":0,
                "failed":0
            }

        data[name]["uses"] += 1

        if success:
            data[name]["success"] += 1
        else:
            data[name]["failed"] += 1

        data[name]["last_used"]=str(datetime.now())

        self.path.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

        return data[name]
