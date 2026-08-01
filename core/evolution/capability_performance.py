
import json
from pathlib import Path

FILE = Path("data/capability_performance.json")


class CapabilityPerformance:

    def __init__(self):
        self.data={}
        self.recent={}
        self.load()


    def record(self,name,success=True):

        # prevent duplicate execution recording
        if self.recent.get(name):
            return self.data.get(name)

        self.recent[name] = True

        if name not in self.data:
            self.data[name]={
                "uses":0,
                "success":0,
                "fail":0,
                "score":0
            }

        self.data[name]["uses"] += 1

        if success:
            self.data[name]["success"] += 1
        else:
            self.data[name]["fail"] += 1


        self.data[name]["score"] = round(
            self.data[name]["success"] /
            self.data[name]["uses"],
            2
        )

        self.save()

        return self.data[name]


    def get(self,name):
        return self.data.get(name)


    def load(self):

        if FILE.exists():
            try:
                self.data=json.loads(
                    FILE.read_text(
                        encoding="utf-8"
                    )
                )
            except:
                self.data={}


    def save(self):

        FILE.parent.mkdir(
            exist_ok=True
        )

        FILE.write_text(
            json.dumps(
                self.data,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )


capability_performance = CapabilityPerformance()
