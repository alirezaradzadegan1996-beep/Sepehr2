
import json
from pathlib import Path


FILE = "data/upgrade_history.json"


class UpgradeMemory:

    def save(self, upgrade):

        Path("data").mkdir(
            exist_ok=True
        )

        try:

            with open(FILE, encoding="utf-8") as f:
                data = json.load(f)

        except:

            data = []


        data.append(upgrade)


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
            "saved": True,
            "status": "stored"
        }


upgrade_memory = UpgradeMemory()
