from core.code_engine import CodeEngine
from core.test_engine import TestEngine
from core.debug_engine import DebugEngine
from core.delivery_engine import DeliveryEngine


class AppBuilder:

    code_engine = CodeEngine()
    test_engine = TestEngine()
    debug_engine = DebugEngine()
    delivery_engine = DeliveryEngine()

    @staticmethod
    def run(project, step):

        if not project:
            return {"message": "❌ پروژه‌ای وجود ندارد."}

        goal = project.get("goal", "app")

        analysis = project.get("analysis", {})
        reasoning = analysis.get("reasoning", {})

        project_type = reasoning.get(
            "type",
            analysis.get(
                "type",
                "general_app"
            )
        )

        # مرحله تحلیل
        if step == 0:
            return {
                "message":
                    "🔍 تحلیل پروژه\n\n"
                    f"نوع برنامه تشخیص داده شد:\n{project_type}"
            }

        # مرحله طراحی
        elif step == 1:
            return {
                "message":
                    "🧩 طراحی راه‌حل\n\n"
                    "ساختار پروژه آماده شد."
            }

        # مرحله ساخت فایل‌ها
        elif step == 2:
            return {
                "message":
                    "📁 ساخت فایل‌ها\n\n"
                    "فایل‌های اولیه ایجاد شدند."
            }

        # مرحله تولید کد (واقعی)
        elif step == 3:
            return {
                "message": AppBuilder.code_engine.generate(
            "projects/" + project["id"],
            project.get("analysis", {})
        )
            }

        # مرحله تست (واقعی)
        elif step == 4:
            test_result = AppBuilder.test_engine.run(project)

            project["test_result"] = test_result

            return {
                "message": test_result,
                "test_result": test_result
            }

        # مرحله دیباگ (واقعی)
        elif step == 5:
            result = AppBuilder.debug_engine.analyze(
                project,
                project.get("test_result")
            )

            if isinstance(result, dict):
                return {
                    "message": result.get("message", "بررسی انجام شد.")
                }

            return {
                "message": str(result)
            }

        # تحویل
        elif step == 6:
            return AppBuilder.delivery_engine.deliver(project)

        return {
            "message": "مرحله نامشخص"
        }
