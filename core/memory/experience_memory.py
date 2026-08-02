import json
from pathlib import Path

from core.memory.experience_normalizer import experience_normalizer


class ExperienceMemory:

    def __init__(self):

        self.file = Path("data/experience_memory.json")
        self.experiences = []

        self.load()


    def load(self):

        if self.file.exists():

            try:
                raw = json.loads(
                    self.file.read_text(encoding="utf-8")
                )

                self.experiences = [
                    experience_normalizer.normalize(item)
                    for item in raw
                    if item is not None
                ]

                self.file.write_text(
                    json.dumps(
                        self.experiences,
                        ensure_ascii=False,
                        indent=2
                    ),
                    encoding="utf-8"
                )

            except Exception:
                self.experiences = []


    def save(self, experience):

        experience = experience_normalizer.normalize(experience)

        self.experiences.append(experience)

        self.file.write_text(
            json.dumps(
                self.experiences,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

        return {
            "experience": experience,
            "status": "stored",
            "count": len(self.experiences)
        }


    def recall(self):

        return {
            "experiences": self.experiences,
            "count": len(self.experiences),
            "status": "recalled"
        }


    def search(self, keyword):

        results = []

        for item in self.experiences:

            if keyword in str(item):
                results.append(item)


        return {
            "results": results,
            "status": "search_completed"
        }



experience_memory = ExperienceMemory()
