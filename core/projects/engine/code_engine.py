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



    def generate(self, project, templates):

        results = []


        for filename, content in templates.items():

            results.append(
                self.create_file(
                    project,
                    filename,
                    content
                )
            )


        return {
            "files": results,
            "status": "code_generated"
        }



code_engine = CodeEngine()
