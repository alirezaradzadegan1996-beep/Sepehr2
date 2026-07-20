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

        level = self.selector.select(project_type)

        for base in self.paths:

            # -------------------------
            # ساختار جدید
            # templates/<type>/<level>/main.py
            # templates/<type>/<level>/main.py.tpl
            # -------------------------
            path = (
                base
                / project_type
                / level
                / filename
            )

            path_tpl = path.with_suffix(path.suffix + ".tpl")

            if path.exists():
                return path.read_text(
                    encoding="utf-8"
                )

            if path_tpl.exists():
                return path_tpl.read_text(
                    encoding="utf-8"
                )

            # -------------------------
            # سازگاری با قالب‌های قدیمی
            # templates/<type>/main.py
            # templates/<type>/main.py.tpl
            # -------------------------
            old_path = (
                base
                / project_type
                / filename
            )

            old_path_tpl = old_path.with_suffix(
                old_path.suffix + ".tpl"
            )

            if old_path.exists():
                return old_path.read_text(
                    encoding="utf-8"
                )

            if old_path_tpl.exists():
                return old_path_tpl.read_text(
                    encoding="utf-8"
                )

        return None

    def list_templates(self, project_type):

        result = []

        level = self.selector.select(project_type)

        for base in self.paths:

            folder = (
                base
                / project_type
                / level
            )

            if folder.exists():
                for f in folder.iterdir():
                    if f.is_file() and f.name not in result:
                        result.append(f.name)

            # قالب‌های قدیمی
            old_folder = (
                base
                / project_type
            )

            if old_folder.exists():
                for f in old_folder.iterdir():
                    if f.is_file() and f.name not in result:
                        result.append(f.name)

        return result
