import os


class CodeEngine:


    name = "code_engine"


    def create_file(self, project, filename, content):

        path = f"projects/{project}/{filename}"

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)


        return {
            "status": "created",
            "file": path
        }



code_engine = CodeEngine()
