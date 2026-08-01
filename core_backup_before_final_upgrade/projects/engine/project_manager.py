
import os
import json


from core.builder.full_builder_engine import builder


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

        with open(path, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        return {
            "status":"saved",
            "file":path
        }


    def build_project(self, request):

        result = builder.build(request)

        project = result.get(
            "project",
            "unknown"
        )

        self.save(
            project,
            result
        )

        return {
            "status":"project_build_completed",
            "result":result
        }



project_manager = ProjectManager()
