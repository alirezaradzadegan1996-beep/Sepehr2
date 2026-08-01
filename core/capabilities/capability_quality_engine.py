
import json
from pathlib import Path


class CapabilityQualityEngine:

    def __init__(self):
        self.memory = Path("data/capability_memory.json")


    def load(self):
        if not self.memory.exists():
            return {}

        try:
            return json.loads(
                self.memory.read_text(encoding="utf-8")
            )
        except:
            return {}


    def score(self, name):

        data = self.load()

        if name not in data:
            return 0


        item = data[name]

        uses = item.get("uses",0)
        success = item.get("success",0)
        failed = item.get("failed",0)


        total = success + failed

        if total == 0:
            return 0


        quality = success / total


        experience_bonus = min(
            uses * 0.05,
            0.25
        )


        final_score = min(
            quality + experience_bonus,
            1.0
        )


        return round(
            final_score,
            3
        )


    def ranking(self):

        data=self.load()

        result=[]

        for name in data:
            result.append(
                {
                    "capability":name,
                    "score":self.score(name)
                }
            )


        return sorted(
            result,
            key=lambda x:x["score"],
            reverse=True
        )
