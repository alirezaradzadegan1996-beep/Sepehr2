
import json
from pathlib import Path
from datetime import datetime


FILE = Path("data/evolution_history.json")


class EvolutionMemory:


    def __init__(self):

        self.history = []

        self.load()


    def record(self, data):

        data["time"] = str(
            datetime.now()
        )

        self.history.append(data)

        self.save()

        return data



    def save(self):

        FILE.parent.mkdir(
            exist_ok=True
        )

        FILE.write_text(
            json.dumps(
                self.history,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )



    def load(self):

        if FILE.exists():

            try:
                self.history = json.loads(
                    FILE.read_text(
                        encoding="utf-8"
                    )
                )

            except:

                self.history = []



evolution_memory = EvolutionMemory()
