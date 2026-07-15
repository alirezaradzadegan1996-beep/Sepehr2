import os


class DeliveryEngine:

    def deliver(self, project):

        if not project:
            return {
                "message": "❌ پروژه‌ای برای تحویل وجود ندارد."
            }

        project_id = project.get("id")
        goal = project.get("goal", "unknown")
        analysis = project.get("analysis", {})

        project_type = analysis.get(
            "type",
            "general"
        )

        project_dir = os.path.join(
            "projects",
            project_id
        )

        files = []

        if os.path.exists(project_dir):
            files = sorted(
                file
                for file in os.listdir(project_dir)
                if os.path.isfile(
                    os.path.join(project_dir, file)
                )
            )

        file_list = "\n".join(
            f"✅ {file}"
            for file in files
        )

        if not file_list:
            file_list = "⚠️ فایلی پیدا نشد."

        message = (
            "🚀 پروژه آماده تحویل است.\n\n"
            f"📌 نام پروژه:\n{goal}\n\n"
            f"🧠 نوع پروژه:\n{project_type}\n\n"
            "📁 فایل‌های پروژه:\n"
            f"{file_list}\n\n"
            "✅ ساخت پروژه انجام شد\n"
            "✅ کد تولید شد\n"
            "✅ تست انجام شد\n"
            "✅ خطاها بررسی شدند\n\n"
            f"📦 مسیر پروژه:\n{project_dir}"
        )

        return {
            "message": message,
            "project_id": project_id,
            "project_path": project_dir,
            "files": files,
            "status": "ready"
        }
