import shutil

path = "core/builder/full_builder_engine.py"

shutil.copy2(
    path,
    path + ".backup_before_real_code"
)

new_code = r'''
import os

from core.projects.engine.code_engine import code_engine
from core.projects.engine.test_engine import test_engine
from core.projects.engine.debug_engine import debug_engine


class FullBuilderEngine:


    def __init__(self):
        self.projects = []


    def analyze(self, request):

        return {
            "request": request,
            "type": "application",
            "status": "analyzed"
        }


    def select_stack(self, project_type):

        return {
            "language": "python",
            "database": "sqlite",
            "interface": "ui",
            "status": "selected"
        }


    def create_project(self, name):

        os.makedirs(
            f"projects/{name}",
            exist_ok=True
        )

        return {
            "project": name,
            "status": "created"
        }


    def generate_code(self, name):

        files = {

"main.py":
'''def main():
    print("Sepehr generated app running")

if __name__ == "__main__":
    main()
''',

"database.py":
'''import sqlite3

def connect():
    return sqlite3.connect("data.db")
''',

"test.py":
'''print("Generated test running")
'''
        }

        result = []

        for filename, content in files.items():

            result.append(
                code_engine.create_file(
                    name,
                    filename,
                    content
                )
            )

        return {
            "files": result,
            "status": "code_generated"
        }


    def test(self, name):

        return test_engine.run(name)


    def debug(self, error):

        return debug_engine.analyze(error)


    def deliver(self, name):

        return {
            "project": name,
            "delivery": "completed",
            "status": "ready"
        }


    def build(self, request):

        name = request.replace(" ", "_")

        pipeline = []

        pipeline.append(
            self.analyze(request)
        )

        pipeline.append(
            self.select_stack("application")
        )

        pipeline.append(
            self.create_project(name)
        )

        pipeline.append(
            self.generate_code(name)
        )

        test_result = self.test(name)

        pipeline.append(
            test_result
        )

        if test_result.get("status") == "failed":

            pipeline.append(
                self.debug(test_result)
            )

        pipeline.append(
            self.deliver(name)
        )


        self.projects.append(name)


        return {
            "project": name,
            "pipeline": pipeline,
            "status": "completed"
        }



builder = FullBuilderEngine()
'''

with open(path, "w", encoding="utf-8") as f:
    f.write(new_code)

print("FULL BUILDER V2 INSTALLED")
