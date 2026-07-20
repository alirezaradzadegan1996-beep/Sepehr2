class ResponseEngine:
    """
    تبدیل خروجی‌های داخلی سپهر به پاسخ انسانی
    """

    def format(
        self,
        result
    ):

        if isinstance(result, str):
            return result


        if not isinstance(result, dict):
            return str(result)


        message = ""


        # -------------------------
        # Project
        # -------------------------

        if result.get(
            "project"
        ):

            message += (
                "🚀 پروژه آماده شد\n\n"
                f"📌 نام پروژه:\n"
                f"{result.get('project')}\n\n"
            )


        # -------------------------
        # Build
        # -------------------------

        build = result.get(
            "build"
        )

        if build:

            message += (
                "📂 ساخت فایل‌ها:\n"
                "✅ انجام شد\n\n"
            )


        # -------------------------
        # Test
        # -------------------------

        test = result.get(
            "test"
        )


        if isinstance(
            test,
            dict
        ):

            if test.get(
                "success"
            ):

                message += (
                    "🧪 تست:\n"
                    "✅ موفق\n\n"
                )

            else:

                message += (
                    "🧪 تست:\n"
                    "❌ ناموفق\n\n"
                )


        # -------------------------
        # Learning
        # -------------------------

        if result.get(
            "status"
        ) == "completed":

            message += (
                "🧠 یادگیری:\n"
                "✅ تجربه پروژه ذخیره شد\n\n"
            )


        # -------------------------
        # Final Status
        # -------------------------

        message += (
            "📌 وضعیت:\n"
            "آماده توسعه 🚀"
        )


        return message
