import os
import json


class TemplateCreator:


    name = "template_creator"


    def create(self, project_type, features):

        path = f"core/templates/generated/{project_type}"

        os.makedirs(
            path,
            exist_ok=True
        )


        files = {

            "main.py.template": self.main_template(project_type),

            "database.py.template": self.database_template(),

            "test.py.template": self.test_template()

        }


        created = []


        for filename, content in files.items():

            file_path = f"{path}/{filename}"

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(content)


            created.append(file_path)


        metadata = {

            "project_type": project_type,

            "features": features,

            "generated_by": "Sepehr Template Creator"

        }


        with open(
            f"{path}/template.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4,
                ensure_ascii=False
            )


        return {

            "template": project_type,

            "files": created,

            "status": "template_created"

        }



    def main_template(self, project_type):

        return f'''
"""
Generated Sepehr Template
Type: {project_type}
"""


def main():

    print("Sepehr generated {project_type}")


if __name__ == "__main__":

    main()

'''



    def database_template(self):

        return '''
import sqlite3


def connect():

    return sqlite3.connect(
        "database.db"
    )

'''



    def test_template(self):

        return '''
def test():

    assert True


if __name__ == "__main__":

    test()

'''



template_creator = TemplateCreator()
