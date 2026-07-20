from core.code_engine import CodeEngine
from core.test_engine import TestEngine
from core.debug_engine import DebugEngine
from core.delivery_engine import DeliveryEngine
from core.project_builder import ProjectBuilder


class AppBuilder:

    code_engine = CodeEngine()
    test_engine = TestEngine()
    debug_engine = DebugEngine()
    delivery_engine = DeliveryEngine()
    project_builder = ProjectBuilder()

    @staticmethod
    def run(project, step):

        if not project:
            return {
                "message": "❌ پروژه‌ای وجود ندارد."
            }

        analysis = project.get("analysis", {})
        reasoning = analysis.get("reasoning", {})

        project_type = reasoning.get(
            "type",
            analysis.get(
                "type",
                "general"
            )
        )

        project_path = "projects/" + project["id"]

        # -------------------------
        # مرحله ۱ : تحلیل
        # -------------------------
        if step == 0:

            return {
                "message":
                    "🔍 تحلیل پروژه\n\n"
                    f"نوع پروژه:\n{project_type}"
            }

        # -------------------------
        # مرحله ۲ : طراحی
        # -------------------------
        elif step == 1:

            return {
                "message":
                    "🧩 طراحی پروژه\n\n"
                    "معماری پروژه آماده شد."
            }

        # -------------------------
        # مرحله ۳ : ساخت فایل‌ها
        # -------------------------
        elif step == 2:

            optimization = analysis.get(
                "optimization",
                {}
            )

            AppBuilder.project_builder.build(
                project_path,
                optimization,
                analysis
            )

            return {
                "message":
                    "📁 فایل‌های پروژه ساخته شدند."
            }

        # -------------------------
        # مرحله ۴ : تولید کد
        # -------------------------
        elif step == 3:

            result = AppBuilder.code_engine.generate(
                project_path,
                analysis
            )

            return {
                "message": result
            }

        # -------------------------
        # مرحله ۵ : تست
        # -------------------------
        elif step == 4:

            test_result = AppBuilder.test_engine.run(project)

            project["test_result"] = test_result

            return {
                "message": test_result,
                "test_result": test_result
            }

        # -------------------------
        # مرحله ۶ : دیباگ
        # -------------------------
        elif step == 5:

            result = AppBuilder.debug_engine.analyze(
                project,
                project.get("test_result")
            )

            if isinstance(result, dict):

                return {
                    "message":
                        result.get(
                            "message",
                            "بررسی انجام شد."
                        )
                }

            return {
                "message": str(result)
            }

        # -------------------------
        # مرحله ۷ : تحویل
        # -------------------------
        elif step == 6:

            return AppBuilder.delivery_engine.deliver(project)

        # -------------------------
        # پایان
        # -------------------------
        return {
            "message": "مرحله نامشخص"
        }
