import re


class DebugEngine:

    def analyze(self, project, test_result=None):

        if not project:
            return {
                "status": "error",
                "message": "❌ پروژه‌ای برای بررسی وجود ندارد."
            }

        goal = project.get(
            "goal",
            "project"
        )

        analysis = {
            "status": "debug",
            "project": goal,
            "error_type": None,
            "file": None,
            "line": None,
            "cause": None,
            "solution": [],
        }


        if not test_result:

            return {
                "status": "optimize",
                "message":
                f"""🛠 بهینه‌سازی پروژه

📌 پروژه:
{goal}

✅ تستی برای بررسی وجود ندارد.
"""
            }


        # پیدا کردن خطا

        if "Traceback" in test_result or "Error" in test_result:

            traceback = test_result


            # نوع خطا

            errors = [
                "ImportError",
                "ModuleNotFoundError",
                "SyntaxError",
                "NameError",
                "TypeError",
                "ValueError",
                "AttributeError"
            ]


            for err in errors:
                if err in traceback:
                    analysis["error_type"] = err
                    break


            # فایل و خط

            match = re.search(
                r'File "(.+?)", line (\d+)',
                traceback
            )

            if match:
                analysis["file"] = match.group(1)
                analysis["line"] = match.group(2)



            # تحلیل Import

            if analysis["error_type"] == "ImportError":

                analysis["cause"] = (
                    "کلاس یا تابع مورد نیاز در فایل مقصد وجود ندارد."
                )

                analysis["solution"] = [
                    "بررسی فایل errors.py",
                    "اضافه کردن کلاس مورد نیاز",
                    "بازسازی template مربوطه",
                ]


            elif analysis["error_type"] == "ModuleNotFoundError":

                analysis["cause"] = (
                    "ماژول مورد نیاز پیدا نشد."
                )

                analysis["solution"] = [
                    "اضافه کردن فایل missing",
                    "بررسی dependency ها",
                ]


            else:

                analysis["cause"] = (
                    "خطای برنامه‌نویسی نیازمند بررسی بیشتر است."
                )

                analysis["solution"] = [
                    "بررسی traceback",
                    "اصلاح کد",
                    "اجرای دوباره تست"
                ]


            return analysis



        return {
            "status": "success",
            "message":
            f"""✅ پروژه سالم است

📌 پروژه:
{goal}

پیشنهاد:
- بهینه‌سازی کد
- افزایش کیفیت
- آماده انتشار
"""
        }
