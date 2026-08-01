import os


class TemplateEngine:


    name = "template_engine"


    def __init__(self):

        self.base = "core/templates/generated"



    def load(self, result):

        files = {}

        if isinstance(result, dict):

            path = result.get("path")

            if not path:

                path = f"{self.base}/{result.get('template')}"

        else:

            path = f"{self.base}/{result}"


        if not os.path.exists(path):

            return files


        for f in os.listdir(path):

            full = os.path.join(
                path,
                f
            )

            with open(
                full,
                "r",
                encoding="utf-8"
            ) as x:

                files[
                    f.replace(".template","")
                ] = x.read()


        return files



    def load_files(self, files):

        result = {}


        for file in files:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                name = file.split("/")[-1]

                name = name.replace(
                    ".template",
                    ""
                )

                result[name] = f.read()


        return result



    def resolve(self, template):

        if isinstance(template, dict):

            if "files" in template:

                return self.load_files(
                    template["files"]
                )


        return self.load(template)



template_engine = TemplateEngine()
