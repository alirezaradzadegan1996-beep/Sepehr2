import os

from core.code_engine import CodeEngine


class ProjectBuilder:

    def __init__(self):
        self.code_engine = CodeEngine()


    def build(self, project_path, plan, analysis=None):

        print("[ProjectBuilder] Building project...")


        folders = plan.get(
            "folders",
            []
        )

        files = plan.get(
            "files",
            []
        )


        # ساخت پوشه‌ها
        for folder in folders:

            path = os.path.join(
                project_path,
                folder
            )

            os.makedirs(
                path,
                exist_ok=True
            )


        # ساخت فایل‌های اولیه
        for file in files:

            path = os.path.join(
                project_path,
                file
            )

            directory = os.path.dirname(path)


            if directory:

                os.makedirs(
                    directory,
                    exist_ok=True
                )


            if not os.path.exists(path):

                with open(
                    path,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write("")


        print("[ProjectBuilder] Files created")


        # تولید کد از Template
        if analysis:

            self.code_engine.generate(
                project_path,
                analysis
            )

            print("[ProjectBuilder] Code generated")


        return True
