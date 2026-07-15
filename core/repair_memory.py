import json
import os


FILE = "data/repair_memory.json"


class RepairMemory:

    def __init__(self):
        self.load()


    def load(self):

        if os.path.exists(FILE):

            try:
                with open(
                    FILE,
                    "r",
                    encoding="utf-8"
                ) as f:
                    self.memory = json.load(f)

            except:
                self.memory = []

        else:
            self.memory = []


    def save(self):

        os.makedirs(
            "data",
            exist_ok=True
        )

        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.memory,
                f,
                ensure_ascii=False,
                indent=4
            )


    def remember(
        self,
        project_type,
        error_type,
        filename,
        solution
    ):

        item = {
            "project_type": project_type,
            "error_type": error_type,
            "file": filename,
            "solution": solution,
            "success": True
        }

        self.memory.append(item)

        self.save()

        return item


    def find(
        self,
        project_type,
        error_type
    ):

        for item in self.memory:

            if (
                item.get("project_type") == project_type
                and
                item.get("error_type") == error_type
            ):
                return item


        return None
