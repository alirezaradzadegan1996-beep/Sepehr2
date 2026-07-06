class Router:

    def route(self, text):
        text = text.strip().lower()

        # =====================
        # SYSTEM COMMANDS
        # =====================
        if text in ["سلام", "hi", "hello"]:
            return {
                "type": "system",
                "response": "سلام 👋 من سپهر هستم. آماده‌ام."
            }

        if text in ["وضعیت", "status"]:
            return {
                "type": "system",
                "response": "سیستم فعال است."
            }

        if text in ["پروژه‌ها", "projects"]:
            return {
                "type": "system",
                "response": "در نسخه بعدی لیست پروژه‌ها نمایش داده می‌شود."
            }

        # =====================
        # DEFAULT → planner
        # =====================
        return {
            "type": "task",
            "data": text
        }
