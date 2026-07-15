import json
import os
import time


FILE = "data/project_knowledge.json"


class ProjectKnowledge:

    def __init__(self):

        self.data = {}

        self.load()


    def load(self):

        if os.path.exists(FILE):

            try:
                with open(
                    FILE,
                    "r",
                    encoding="utf-8"
                ) as f:

                    self.data = json.load(f)

            except:

                self.data = {}

        else:

            self.data = {}


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
                self.data,
                f,
                ensure_ascii=False,
                indent=4
            )


    def add_project_experience(
        self,
        project_type,
        experience
    ):

        if project_type not in self.data:

            self.data[project_type] = {

                "successful_patterns": [],

                "common_errors": [],

                "solutions": [],

                "projects_count": 0
            }


        item = self.data[project_type]


        item["projects_count"] += 1


        for feature in experience.get(
            "features",
            []
        ):

            if feature not in item["successful_patterns"]:

                item["successful_patterns"].append(
                    feature
                )


        if experience.get(
            "error"
        ):

            if experience["error"] not in item["common_errors"]:

                item["common_errors"].append(
                    experience["error"]
                )


        if experience.get(
            "solution"
        ):

            if experience["solution"] not in item["solutions"]:

                item["solutions"].append(
                    experience["solution"]
                )


        item["updated"] = time.time()


        self.save()


        return {
            "saved": True,
            "type": project_type,
            "projects_count": item["projects_count"]
        }


    def get_knowledge(
        self,
        project_type
    ):

        return self.data.get(
            project_type,
            {
                "successful_patterns": [],
                "common_errors": [],
                "solutions": [],
                "projects_count": 0
            }
        )
