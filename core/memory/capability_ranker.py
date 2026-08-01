import json
import os

PRIORITY_FILE = "data/capability_scores.json"
MEMORY_FILE = "data/consolidated_memory.json"


class CapabilityRanker:

    def __init__(self):
        self.load()

    def load(self):

        if os.path.exists(PRIORITY_FILE):
            with open(PRIORITY_FILE, encoding="utf-8") as f:
                self.priority = json.load(f)
        else:
            self.priority = {}

        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, encoding="utf-8") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}


    def rank(self, candidates):

        if not candidates:
            return None


        ranked = []

        for item in candidates:

            name = item.get("name")
            score = item.get("score",0)

            final_score = score


            # Priority Memory boost
            p = self.priority.get(name)

            if p:
                final_score += (
                    p.get("priority",0) / 100
                )


            # Consolidated memory boost
            m = self.memory.get(name)

            if m:

                final_score += (
                    m.get("confidence",0)
                    * 2
                )


                final_score += (
                    m.get("experience_count",0)
                    * 0.1
                )


            ranked.append(
                {
                    "capability":name,
                    "score":round(final_score,2)
                }
            )


        ranked.sort(
            key=lambda x:x["score"],
            reverse=True
        )


        return ranked[0]


capability_ranker = CapabilityRanker()
