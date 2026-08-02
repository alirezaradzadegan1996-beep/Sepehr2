import json
from datetime import datetime


class StateWriter:


    def save(self, data):

        data["last_update"] = str(datetime.now())

        with open(
            "data/self_completion/project_state.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )


state_writer = StateWriter()
