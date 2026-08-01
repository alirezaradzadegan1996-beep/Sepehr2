
from pathlib import Path
import json


class CapabilityExperienceSelector:

    def __init__(self):
        self.memory = Path("data/capability_memory.json")


    def load(self):

        if self.memory.exists():

            return json.loads(
                self.memory.read_text(encoding="utf-8")
            )

        return {}


    def score(self, capability):

        data = self.load()

        if capability not in data:
            return 0

        item = data[capability]

        uses = item.get("uses", 0)
        success = item.get("success", 0)

        if uses == 0:
            return 0

        return success / uses


    def rank(self, capabilities):

        result = []

        for c in capabilities:

            result.append(
                {
                    "capability": c,
                    "score": self.score(c)
                }
            )

        result.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return result


    def choose(self, capabilities):

        ranked = self.rank(capabilities)

        if ranked:
            return ranked[0]["capability"]

        return None
