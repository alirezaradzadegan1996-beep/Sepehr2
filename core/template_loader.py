from pathlib import Path
from core.template_selector import TemplateSelector


class TemplateLoader:

    def __init__(self):

        self.selector = TemplateSelector()

        self.paths = [
            Path("templates"),
            Path("core/templates")
        ]


    def load(self, project_type, filename):

        level = self.selector.select(
            project_type
        )


        for base in self.paths:

            # ساختار جدید:
            # templates/
            #   calculator/
            #       basic/
            #           main.py
            #
            #       advanced/
            #           main.py

            path = (
                base
                /
                project_type
                /
                level
                /
                filename
            )


            if path.exists():

                return path.read_text(
                    encoding="utf-8"
                )


            # سازگاری با قالب‌های قدیمی
            old_path = (
                base
                /
                project_type
                /
                filename
            )


            if old_path.exists():

                return old_path.read_text(
                    encoding="utf-8"
                )


        return None



    def list_templates(self, project_type):

        result = []

        level = self.selector.select(
            project_type
        )


        for base in self.paths:

            folder = (
                base
                /
                project_type
                /
                level
            )


            if folder.exists():

                for f in folder.iterdir():

                    if (
                        f.is_file()
                        and f.name not in result
                    ):
                        result.append(
                            f.name
                        )


            # قالب قدیمی
            old_folder = (
                base
                /
                project_type
            )


            if old_folder.exists():

                for f in old_folder.iterdir():

                    if (
                        f.is_file()
                        and f.name not in result
                    ):
                        result.append(
                            f.name
                        )


        return result
