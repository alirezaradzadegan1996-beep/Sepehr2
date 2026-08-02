import os
import json
from datetime import datetime


STATE_FILE = "data/self_completion/project_state.json"


class ProjectAnalyzer:

    def analyze(self):

        result = {
            "time": str(datetime.now()),
            "files": 0,
            "modules": [],
            "status": "analyzed"
        }

        for root, dirs, files in os.walk("core"):

            for file in files:

                if file.endswith(".py"):

                    result["files"] += 1

                    path = os.path.join(
                        root,
                        file
                    )

                    result["modules"].append(
                        path
                    )


        with open(
            STATE_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                result,
                f,
                ensure_ascii=False,
                indent=2
            )


        return result


project_analyzer = ProjectAnalyzer()
