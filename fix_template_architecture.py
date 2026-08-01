
from pathlib import Path


# Fix FullBuilderEngine
path = Path("core/builder/full_builder_engine.py")

text = path.read_text(encoding="utf-8")


old = """
        template = adaptive_template_manager.get_template(
            intent["project_type"],
            intent["features"]
        )


        templates = template_engine.load(
            template
        )
"""


new = """
        template = adaptive_template_manager.get_or_create_template(
            intent["project_type"],
            intent["features"]
        )


        templates = template_engine.resolve(
            template
        )
"""


text=text.replace(old,new)

path.write_text(text,encoding="utf-8")


# Fix Template Engine
path = Path("core/templates/template_engine.py")

text = path.read_text(encoding="utf-8")


if "def resolve" not in text:

    text += """



    def resolve(self, template):

        # اگر خروجی Template Creator بود
        if isinstance(template, dict):

            if "files" in template:

                return self.load_files(
                    template["files"]
                )


        # اگر اسم Template بود
        return self.load(template)



    def load_files(self, files):

        result={}

        for file in files:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                name=file.split("/")[-1]
                name=name.replace(
                    ".template",
                    ""
                )

                result[name]=f.read()


        return result

"""


path.write_text(text,encoding="utf-8")


print("Template Architecture Fixed")

