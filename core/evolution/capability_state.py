
import json
from pathlib import Path


STATE_FILE = Path(
    "data/capability_state.json"
)


class CapabilityState:


    def __init__(self):

        self.states = {}

        self.load()



    def update(self, name, data):

        self.states[name] = data

        self.save()

        return self.states[name]



    def get(self, name):

        return self.states.get(
            name,
            {}
        )



    def save(self):

        STATE_FILE.parent.mkdir(
            exist_ok=True
        )

        STATE_FILE.write_text(
            json.dumps(
                self.states,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )



    def load(self):

        if STATE_FILE.exists():

            try:

                self.states = json.loads(
                    STATE_FILE.read_text(
                        encoding="utf-8"
                    )
                )

            except:

                self.states = {}



capability_state = CapabilityState()
