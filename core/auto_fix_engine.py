from pathlib import Path
import shutil

from core.repair_memory import RepairMemory


class AutoFixEngine:

    def __init__(self):

        self.templates = Path(
            "templates"
        )

        self.repair_memory = RepairMemory()


    def analyze_fix(self, project, debug_result):

        if not debug_result:
            return {
                "fixed": False,
                "reason": "no debug data"
            }


        return {
            "fixed": False,
            "error_type": debug_result.get(
                "error_type"
            ),
            "file": debug_result.get(
                "file"
            ),
            "action": "template_compare"
        }


    def apply_fix(
        self,
        project_path,
        project_type,
        filename,
        error_type="unknown"
    ):

        # بررسی تجربه قبلی
        old_fix = self.repair_memory.find(
            project_type,
            error_type
        )


        if old_fix:

            print(
                "[RepairMemory] Using previous solution"
            )


        target = (
            Path(project_path)
            /
            filename
        )


        template_candidates = [

            self.templates
            / project_type
            / "advanced"
            / filename,


            self.templates
            / project_type
            / "basic"
            / filename,


            self.templates
            / project_type
            / filename
        ]


        for template in template_candidates:

            if template.exists():

                shutil.copy(
                    template,
                    target
                )


                result = {
                    "fixed": True,
                    "file": filename,
                    "source": str(template),
                    "target": str(target),
                    "memory_used": bool(old_fix)
                }


                # ذخیره تجربه تعمیر
                self.repair_memory.remember(
                    project_type,
                    error_type,
                    filename,
                    "template_replace"
                )


                return result


        return {
            "fixed": False,
            "file": filename,
            "reason": "template not found"
        }
