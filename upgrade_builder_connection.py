import shutil
import os

files = [
    "core/runtime/runtime_router_bridge.py",
    "core/projects/engine/project_manager.py"
]

for f in files:
    if os.path.exists(f):
        shutil.copy2(f, f + ".backup_builder_upgrade")
        print("backup:", f)


# Patch ProjectManager
path = "core/projects/engine/project_manager.py"

with open(path, "w", encoding="utf-8") as f:
    f.write('''
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
''')

print("ProjectManager upgraded")


# Patch Runtime Bridge
path = "core/runtime/runtime_router_bridge.py"

text = open(path,encoding="utf-8").read()

if "project_manager" not in text:

    text = text.replace(
        "from core.decision.decision_core import decision_core",
        "from core.decision.decision_core import decision_core\nfrom core.projects.engine.project_manager import project_manager"
    )

    text = text.replace(
'''return {
                "route":"project_builder",
                "action":"build_project",
                "status":"sent_to_builder"
            }''',
'''return project_manager.build_project(text)'''
    )


    open(path,"w",encoding="utf-8").write(text)

    print("Runtime Router upgraded")

else:
    print("Runtime already patched")


print("BUILD CONNECTION UPGRADE COMPLETE")
