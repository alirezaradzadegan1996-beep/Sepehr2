import os
import json


class ProjectManager:


    name = "project_manager"


    def create(self, name):

        path = f"projects/{name}"

        os.makedirs(
            path,
            exist_ok=True
        )

        return {
            "project": name,
            "path": path,
            "status": "created"
        }


    def save(self, project, data):

        path = f"projects/{project}/project.json"

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        with open(
            path,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


        return {
            "status": "saved",
            "file": path
        }


project_manager = ProjectManager()
