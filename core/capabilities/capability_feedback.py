
import json
from pathlib import Path
from datetime import datetime


class CapabilityFeedback:

    def __init__(self):

        self.path = Path(
            "data/capability_feedback.json"
        )

        if not self.path.exists():
            self.path.write_text(
                "{}",
                encoding="utf-8"
            )


    def record(self, capability, success=True):

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )


        if capability not in data:

            data[capability] = {
                "success":0,
                "failed":0,
                "last_feedback":None
            }


        if success:
            data[capability]["success"] += 1

        else:
            data[capability]["failed"] += 1


        data[capability]["last_feedback"] = (
            str(datetime.now())
        )


        self.path.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=4
            ),
            encoding="utf-8"
        )


        return data[capability]


    def get(self, capability):

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        return data.get(
            capability,
            {}
        )
