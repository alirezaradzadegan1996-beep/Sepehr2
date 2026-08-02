
import json
from pathlib import Path


FILE = "data/evolution_history.json"


class EvolutionMemoryIntegration:

    def save(self, event):

        Path("data").mkdir(
            exist_ok=True
        )

        try:
            with open(FILE, encoding="utf-8") as f:
                data = json.load(f)

        except:
            data = []


        data.append(event)


        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )


        return {
            "status":"saved",
            "event":event
        }


evolution_memory_integration = EvolutionMemoryIntegration()
