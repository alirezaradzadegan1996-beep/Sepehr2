
import json
from pathlib import Path


FILE = "data/learning_experiences.json"


class ExperienceStore:

    def save(self, experience):

        Path("data").mkdir(
            exist_ok=True
        )

        try:

            with open(FILE, encoding="utf-8") as f:
                data = json.load(f)

        except:

            data = []


        data.append(experience)


        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )


        return {
            "experience": experience,
            "status": "stored"
        }


experience_store = ExperienceStore()
